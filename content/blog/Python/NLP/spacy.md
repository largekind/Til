---
title: "Spacy"
date: 2023-06-28T22:32:08+09:00
categories: ["Python"]
tags: ["AI", "NLP", "Python"]
---
# Spacy

## 概要

自然言語処理をおこなうためのライブラリ。

固有表現抽出や構文解析などの処理がいろいろ可能。

詳細は別途記述

[詳細](https://spacy.io/)

## 独自のエンティティの学習方法

NER(固有表現抽出)で自分が定義したラベルを抽出してほしい場合のサンプルコード。

[参考資料](https://stackoverflow.com/questions/69181078/spacy-how-do-you-add-custom-ner-labels-to-a-pre-trained-model)

``` python
import spacy
import random
from spacy import util
from spacy.tokens import Doc
from spacy.training import Example
from spacy.language import Language

def print_doc_entities(_doc: Doc):
    # 文書中のエンティティを出力する
    if _doc.ents:
        for _ent in _doc.ents:
            print(f"     {_ent.text} {_ent.label_}")
    else:
        print("     NONE")

def customizing_pipeline_component(nlp: Language):
    # トレーニングデータの定義
    train_data = [
        ('We need to deliver it to Festy.', [(25, 30, 'DISTRICT')]),  # 'Festy'を地区名としてラベル付け
        ('I like red oranges', [])  # エンティティなしの例
    ]

    # トレーニング前の結果を出力
    print(f"\nResult BEFORE training:")
    doc = nlp(u'I need a taxi to Festy.')
    print_doc_entities(doc)

    # 'ner'以外のパイプラインコンポーネントを無効化
    disabled_pipes = []
    for pipe_name in nlp.pipe_names:
        if pipe_name != 'ner':
            nlp.disable_pipes(pipe_name)
            disabled_pipes.append(pipe_name)

    print("   Training ...")
    optimizer = nlp.create_optimizer()
    # トレーニングの実行
    for _ in range(25):
        random.shuffle(train_data)
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)  # テキストからDocオブジェクトを作成
            example = Example.from_dict(doc, {"entities": entity_offsets})  # Docオブジェクトとエンティティの情報からExampleオブジェクトを作成
            nlp.update([example], sgd=optimizer)  # Exampleオブジェクトを使ってモデルを更新

    # 無効化したパイプラインコンポーネントを再度有効化
    for pipe_name in disabled_pipes:
        nlp.enable_pipe(pipe_name)

    # トレーニング後の結果を出力
    print(f"Result AFTER training:")
    doc = nlp(u'I need a taxi to Festy.')
    print_doc_entities(doc)

```

## excelで定義したデータセットからtrain_dataの作成を行う方法

以下サンプルコードを参照

``` python
import pandas as pd

# Excel ファイルを読み込む
df = pd.read_excel('your_file.xlsx')

# ラベルを取得
labels = df.columns[1:]

# 空のリストを作成
train_data = []

# 各行を処理
for index, row in df.iterrows():
    # ラベルリストを初期化
    entity_list = []
    for label in labels:
        # エンティティ（抽出パラメータ）を取得
        entity = row[label]
        # エンティティが存在し、且つエンティティが元の文字列内に存在する場合、その位置を取得
        if pd.notna(entity) and entity in row[0]:
            start = row[0].find(entity)
            end = start + len(entity)
            entity_list.append((start, end, label))
    # トレーニングデータリストに追加
    train_data.append((row[0], entity_list))

print(train_data)
```

## NLPモデルの保存/読み出し

以下で対応可能
- 保存
> nlp.to_disk("/path/to/your/model")
- 読込
> nlp = spacy.load("/path/to/your/model")

## NLPモデルで取得した情報のdataframe化

NLPモデルで情報を抽出するときのサンプルコード。

重複した情報が出る場合はワーニングを表示する

``` python
import spacy
import pandas as pd

# モデルを読み込む
nlp = spacy.load("/path/to/your/model")

# 新しいテキストデータ 例えばパス群など
texts = glob.glob("hoge")

# 各テキストに対するエンティティの辞書を格納するリスト
entities_data = []

# 各テキストに対してモデルを適用
for text in texts:
    doc = nlp(text)
    # エンティティの辞書を作成（エンティティのラベルをキー、エンティティのテキストを値とする）
    entities_dict = {}
    for ent in doc.ents:
        if ent.label_ in entities_dict:
            print(f"Warning: multiple entities with label '{ent.label_}' detected in text: '{text}'")
        entities_dict[ent.label_] = ent.text
    entities_data.append(entities_dict)

# DataFrameを作成
df = pd.DataFrame(entities_data)

# DataFrameを表示
print(df)
```