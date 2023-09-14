---
title: "評価関数"
date: 2023-08-20T23:06:45+09:00
categories: ["DXQuest"]
tags: ["DXQuest", "AI_Beginner"]
---
# 評価関数

## 概要

- 学んだこと
  - 評価関数
    - モデルの性能を定量的に表すための関数
    - タスクに応じて適切な評価関数を作成する必要がある
    - 予測精度とKPIが関連付けられれば、費用対効果を作れられる
  - 代表的なタスクと使用する評価関数
    - 回帰
      - MSRやR^2係数など
    - 分類
      - Accurary/Precision/Recall/AUC/F値など
    - 推薦・検索
      - mAP@N/nDCGなど
    - 物体(領域)検出
      - IOU/mAP

## 回帰問題における評価関数
  
- 学んだこと
  - MAE(Mean Absolute Error)
    - 絶対平均誤差
    - 実測値と予測値の差の平均で損失を出すやつ
    - 外れ値があってもあまり影響がない特徴を持つ
  - RMSE(Root Mean Squared Error)
   - 平均平方に上戸鎖
   - 実測値と予測値の差の2乗の平均の平方根で損失を出すやつ
   - 外れ値が出る場合に誤差が大きくなる特徴を持つ
  - MAPE(Mean Absolutte Percentage Error)
    - 平均絶対誤差
    - 実測値に対する誤差の割合をもとに算出する指標 相対誤差に近い
    - スケールが異なるデータの誤差を比較しやすい
    - **実測値に0が入ると使用不可になる**
      - その場合はSMAPEがあるのでそちらを利用する
  - R^2(決定係数)
    - データそのもののばらつき（分散）と予測値の誤差を求める方式
    - 重回帰分析でよく使用される
    - 1に近いほど予測のばらつきが実測値と近い形となる
      
## 分類問題における評価関数

- 学んだこと
  - 混合行列(Confution Matrix)
    - TF/PNで出せる次のような図[^ConfutionMatrix]
  - Accuracy(正解率)
    - 予測結果が実際にあたっていた割合
    - 欠陥検出といった、negativeの割合が少ない予測には使えない
  - Precision(適合率)
    - 予測してPositiveだったもののうち、実際にPositiveだったもの
    - スパムメールなど、誤判定はなくしたいものに使われる
  - Recall(再現率)
    - 実際にPositiveのもののうち、予測がPositiveだったもの
    - 見落としなどを無くしたい場合に使われるもの。欠陥検出など
    - Precisionとはトレードオフの関係
  - F値
    - Precision/Recallの両方を加味したもの。1のほうがよい
  - ROC曲線
    - 二値分類で閾値を変化したとき、モデル性能がどう変わるかを可視化するもの
      - 縦軸をRecall/横軸をFPR(偽陽性率)として算出する
  - AUC
    - Area Under the Curve
    - ROC曲線の下側の面積を値とするもの。1.0が理想だが基本ない
    - AUCが0.5だと完全ランダムとなる
  
[^ConfutionMatrix]:
    |  |positiveな予測結果|negativeな予測結果| 
    |:----|:----|:----|
    |実際のpositiveな結果|True Positive (TP)|False Ngative (FN)|
    |実際のnegativeな結果|False Positive (FP)|True Negative (TN)|

## 推薦・検索問題における評価関数

- 学んだこと
  - 検索エンジンといったもので用いる評価関数がある
    - よくある評価値やGood/Badなどのものもこちら
  - Precision@k
    - 検索したとき、上位k件に実際に適合したアイテムが入ってる割合
  - Recall@k
    - 全適合アイテムから、実際に適合したk件のアイテムの割合
  - AP(Average Precision)
    - 適合アイテムが得られた時点での適合率の平均をとった値
  - MAP (Mean Average Precision)
    - 全ユーザーでのAP値
  - DCG(Discounted Cumulate Gain)
    - 推薦したアイテムの関連度に重みづけして合計したもの
  - nDCG(normalized DCG)
    - DCGに対して理想的な順位付けを行ったときのDCG_perfectで割った値
    - ただのDCGに正規化しただけのもの