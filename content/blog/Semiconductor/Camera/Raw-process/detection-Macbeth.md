---
title: "Detection Macbeth"
date: 2023-12-17T20:03:09+09:00
draft: True
categories: ["Semiconductor"]
tags: ["Semiconductor", "Camera", "Raw-process"]
---
# Detection Macbeth

## 概要

マクベスの検出検討を行う

## 仮ソース

``` python
import cv2
import numpy as np

def detect_macbeth_chart(grayscale_image):
    # 平滑化を行い、誤判定を減らす
    blurred = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    
    # エッジ検出
    edges = cv2.Canny(blurred, 50, 150)
    
    # 輪郭検出
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # マクベスチャートの輪郭を見つける
    macbeth_contours = []
    for contour in contours:
        # 近似した輪郭を取得
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        # 四角形かつ直線的な輪郭を探す
        if len(approx) == 4 and cv2.isContourConvex(approx):
            _, _, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 1.3 < aspect_ratio < 1.7:  # マクベスチャートのおおよそのアスペクト比
                macbeth_contours.append(approx)
    
    return macbeth_contours

# グレースケール画像の読み込み
grayscale_image = load_grayscale_image('path_to_raw_image.raw')

# 2次元データを扱うために適切な形状に変換
grayscale_image = grayscale_image.reshape((*grayscale_image.shape, 1))

# マクベスチャートの検出
macbeth_contours = detect_macbeth_chart(grayscale_image[..., 0])

# 検出結果の表示
for contour in macbeth_contours:
    # 検出された輪郭を元の画像に描画
    cv2.polylines(grayscale_image, [contour], True, (255), 2)

def auto_canny(image, sigma=0.33):
    # 画像の中央値を計算
    v = np.median(image)
    
    # 閾値を自動的に決定
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    
    # Cannyエッジ検出を適用
    edged = cv2.Canny(image, lower, upper)
    
    return edged

```

watershedを用いた版

``` python
import cv2
import numpy as np

def apply_watershed(grayscale_image):
    # ノイズ除去のための平滑化
    blurred = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Sure background areaの特定
    dilated = cv2.dilate(blurred, np.ones((7, 7), np.uint8), iterations=2)

    # Sure foreground area（前景）の特定
    dist_transform = cv2.distanceTransform(blurred, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Unknown region（不明な領域）の特定
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(dilated, sure_fg)

    # ラベリング
    _, markers = cv2.connectedComponents(sure_fg)

    # ウォーターシェッドのマーカーとして1を足す（背景は0のため）
    markers = markers + 1

    # Unknown regionに対して0のマーカーを設定
    markers[unknown == 255] = 0

    # ウォーターシェッド変換を適用
    markers = cv2.watershed(cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR), markers)

    return markers

def detect_macbeth_chart(grayscale_image):
    markers = apply_watershed(grayscale_image)
    
    # マクベスチャートの領域を見つけるための輪郭検出
    macbeth_contours = []
    for label in np.unique(markers):
        if label == 0 or label == -1:
            continue

        mask = np.zeros(grayscale_image.shape, dtype="uint8")
        mask[markers == label] = 255

        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if cnts:
            largest_contour = max(cnts, key=cv2.contourArea)
            macbeth_contours.append(largest_contour)

    return macbeth_contours

# 画像を読み込む
# 実際には画像ファイルから読み込んだグレースケール画像データを使用します。
grayscale_image = np.random.rand(800, 600) * 255
grayscale_image = grayscale_image.astype(np.uint8)

# マクベスチャートの検出
macbeth_contours = detect_macbeth_chart(grayscale_image)

# 結果の表示
for contour in macbeth_contours:
    cv2.drawContours(grayscale_image, [contour], -1, (255), 2)

cv2.imshow('Detected Macbeth Chart', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
template matchingを使う版テスト

``` python
import cv2
import numpy as np

def match_template(image, template):
    best_match = None
    best_value = 0
    best_scale = 1
    best_angle = 0

    for scale in np.linspace(0.5, 1.5, 20):
        for angle in range(0, 360, 10):
            resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            rows, cols = resized_template.shape[:2]
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            rotated_template = cv2.warpAffine(resized_template, M, (cols, rows))

            result = cv2.matchTemplate(image, rotated_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > best_value:
                best_value = max_val
                best_match = max_loc
                best_scale = scale
                best_angle = angle

    return best_match, best_scale, best_angle, best_value

def find_macbeth_patches(image, template):
    best_match, best_scale, best_angle, _ = match_template(image, template)

    # マクベスチャートの各パッチの座標を計算
    t_height, t_width = template.shape[:2]
    patch_width = t_width / 6 * best_scale
    patch_height = t_height / 4 * best_scale

    patches = []
    for i in range(6):
        for j in range(4):
            top_left_x = best_match[0] + i * patch_width
            top_left_y = best_match[1] + j * patch_height
            bottom_right_x = top_left_x + patch_width
            bottom_right_y = top_left_y + patch_height

            top_left = (int(top_left_x), int(top_left_y))
            bottom_right = (int(bottom_right_x), int(bottom_right_y))

            patches.append((top_left, bottom_right))

    return patches

# ダミーの画像とテンプレートを生成（テスト用）
image = np.random.rand(800, 600) * 255
image = image.astype(np.uint8)
template = np.random.rand(100, 150) * 255
template = template.astype(np.uint8)

# マクベスチャートの各パッチの座標を検出
macbeth_patches = find_macbeth_patches(image, template)

# 各パッチを描画
for top_left, bottom_right in macbeth_patches:
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# 結果の表示
cv2.imshow('Macbeth Chart Patches', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

SURF版

``` python
import cv2
import numpy as np

def detect_macbeth_chart_with_surf(image, template):
    # SURF検出器の初期化
    surf = cv2.xfeatures2d.SURF_create(400)

    # テンプレートと画像のキーポイントとディスクリプタを検出
    keypoints_template, descriptors_template = surf.detectAndCompute(template, None)
    keypoints_image, descriptors_image = surf.detectAndCompute(image, None)

    # FLANNマッチャーを使用してディスクリプタ間のマッチングを行う
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors_template, descriptors_image, k=2)

    # レシオテストを使用して良いマッチングを選択
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # ホモグラフィを計算
    if len(good_matches) > 4:
        src_pts = np.float32([keypoints_template[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_image[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        # ホモグラフィを使用して各パッチの位置を計算
        h, w = template.shape[:2]
        patch_coords = []
        patch_width = w / 6
        patch_height = h / 4
        for i in range(6):
            for j in range(4):
                pt1 = np.array([i * patch_width, j * patch_height, 1]).reshape(-1, 1)
                pt2 = np.array([(i + 1) * patch_width, j * patch_height, 1]).reshape(-1, 1)
                pt3 = np.array([(i + 1) * patch_width, (j + 1) * patch_height, 1]).reshape(-1, 1)
                pt4 = np.array([i * patch_width, (j + 1) * patch_height, 1]).reshape(-1, 1)
                dst_pt1 = np.matmul(H, pt1)
                dst_pt2 = np.matmul(H, pt2)
                dst_pt3 = np.matmul(H, pt3)
                dst_pt4 = np.matmul(H, pt4)
                dst_pt1 /= dst_pt1[2]
                dst_pt2 /= dst_pt2[2]
                dst_pt3 /= dst_pt3[2]
                dst_pt4 /= dst_pt4[2]
                patch_coords.append((dst_pt1[:2], dst_pt2[:2], dst_pt3[:2], dst_pt4[:2]))

        return patch_coords
    else:
        # 十分なマッチングが見つからない場合
        return None

# ダミーの画像とテンプレートを生成（テスト用）
image = np.random.rand(800, 600) * 255
image = image.astype(np.uint8)
template = np.random.rand(100, 150) * 255
template = template.astype(np.uint8)

# マクベスチャートのパッチ座標を検出
macbeth_patches = detect_macbeth_chart_with_surf(image, template)

# 結果の表示
if macbeth_patches is not None:
    for patch in macbeth_patches:
        pts = np.array([patch[0][0], patch[1][0], patch[2][0], patch[3][0]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
    cv2.imshow('Detected Macbeth Chart', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("マクベスチャートは検出されませんでした。")

```

bmp検出

``` python
import cv2
import numpy as np
from colour_checker_detection.detection.common import (
    DTYPE_FLOAT_DEFAULT,
    SETTINGS_DETECTION_COLORCHECKER_CLASSIC,
    DataDetectionColourChecker,
    as_int32_array,
    quadrilateralise_contours,
    sample_colour_checker,
)
from colour_checker_detection.detection.inference import SETTINGS_INFERENCE_COLORCHECKER_CLASSIC, inferencer_default
from colour.utilities import (
    Structure,
    as_int_scalar,
    is_string,
)

from colour.hints import (
    Any,
    ArrayLike,
    Callable,
    Dict,
    NDArrayFloat,
    NDArrayInt,
    Tuple,
    Union,
    cast,
)
from colour.io import convert_bit_depth, read_image, write_image

def calculate_checker_size_from_contour(contour):
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    width = np.linalg.norm(box[0] - box[1])
    height = np.linalg.norm(box[1] - box[2])

    return width, height

def calculate_swatch_areas(color_checker_contour, settings):
    checker_width, checker_height = calculate_checker_size_from_contour(color_checker_contour)
    swatch_width = checker_width / settings["swatches_horizontal"]
    swatch_height = checker_height / settings["swatches_vertical"]

    swatch_areas = []
    for row in range(settings["swatches_vertical"]):
        for col in range(settings["swatches_horizontal"]):
            top_left = (col * swatch_width, row * swatch_height)
            bottom_right = ((col + 1) * swatch_width, (row + 1) * swatch_height)
            swatch_areas.append((top_left, bottom_right))

    return swatch_areas

INFERRED_CLASSES: Dict = {0: "ColorCheckerClassic24"}

def detect_colour_checkers_inference_modified(image, settings):
    if inferencer_kwargs is None:
        inferencer_kwargs = {}

    settings = Structure(**SETTINGS_INFERENCE_COLORCHECKER_CLASSIC)

    swatches_horizontal = settings.swatches_horizontal
    swatches_vertical = settings.swatches_vertical
    working_width = settings.working_width
    working_height = settings.working_height

    results = inferencer_default(image, **inferencer_kwargs)

    if is_string(image):
        image = read_image(cast(str, image))
    else:
        image = convert_bit_depth(
            image, DTYPE_FLOAT_DEFAULT.__name__  # pyright: ignore
        )

    image = cast(Union[NDArrayInt, NDArrayFloat], image)

    rectangle = as_int32_array(
        [
            [0, 0],
            [0, working_height],
            [working_width, working_height],
            [working_width, 0],
        ]
    )



    colour_checkers_data = []
    for result_confidence, result_class, result_mask in results:
        if result_confidence < settings.inferred_confidence:
            continue

        if settings.inferred_class != INFERRED_CLASSES[int(result_class)]:
            continue

        mask = cv2.resize(
            result_mask,
            image.shape[:2][::-1],
            interpolation=cv2.INTER_BITS,
        )

        contours, _hierarchy = cv2.findContours(
            mask.astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )

        for quadrilateral in quadrilateralise_contours(contours):
            # ここで、`sample_colour_checker` 関数の代わりに、
            # 輪郭の座標情報を直接取得
            checker_contour = quadrilateral
            swatch_areas = calculate_swatch_areas(checker_contour)

            colour_checkers_data.append({
                "contour": checker_contour,
                "swatch_areas": swatch_areas
            })

    return colour_checkers_data

```