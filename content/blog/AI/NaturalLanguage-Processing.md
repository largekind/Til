---
title: "自然言語処理 (NLP)"
date: 2023-04-05T00:00:00+09:00
tags: ["Python", "AI"]
categories: ["AI"]
---
# 自然言語処理 (NLP)

Natural Language Processing : NLP

人間がしゃべる言葉をコンピューターで処理させようというやつ

LSTMとかRNNとかSeq2Seqとか時系列的に処理していくアレ

## 単語埋め込み

単語をベクトル化すること。コンピュータに入力できるように数値化する

## Word2vec

単語をベクトル化するため、MLP(Multi Layer Perseptron : 全結合層)に入れて数値化する手法

実質的に単語 -> ベクトルにするためのAEに近いイメージ

### CBOW

単語をベクトル化するための学習方法の１つ。

単語を与えられた時、その空白を埋める形で単語の間の単語を予測をする学習法
(穴埋め問題形式で単語間の情報を学習)

例 : my _____ is  ->  間に来るのはnameなのかと予測・学習

### Skip-gram

単語をベクトル化するための学習方法の１つ。

単語を与えられたとき、その前後の単語を予測するような学習法
（マジカルバナナ形式で単語の前後を学習）

例 : ____ name ____ -> my name isとか？色々予測

## 機械翻訳

Google翻訳とかDeepLとか。

翻訳の手法に*ルールベース*と*統計ベース*の2種類がある

また、評価法としてPerplextiyとBLEUが使われる
### RBMT (Rule-Based Machine Translation)

ルールベースでの翻訳手法

予め登録済みのルールを適応して、訳文を出力する手法。

「文法ベースでの翻訳」に近い。論文とかへの解釈は精度高いが、口語とかスラングに弱い

### SMT (Statisitical Machine Translation)

統計ベースでの翻訳手法

文語・口語問わず訳せるかつ、データが充実しているのであれば人間を超える。
その代わり、当然データ依存かつデータが少ない場合は別の意味に問われてしまうなどがある。

**Deep Leaningを用いた翻訳はSMTとなる**

## 機械翻訳の評価指標

### Perplexity

「次の単語として絞り込めた候補単語数」を図る評価指標

つまり、「文法的にその文は変じゃないよね」を図る指標

### BLEU (bilingual evaluation understudy)

プロの翻訳者の役と近いかどうか、正解と生成した訳がどれだけ類似しているかを出す指標

類語などが考慮されずバリエーションも多い問題があるが、それでもこちらがスタンダードな指標となっている


### N-gram

ある文章を連続するn文字/n単語の塊に分割する手法。splitに近い

これとモデルを組み合わせて、「前何個までの情報をもとに文を予測するか」を推測する(**n-gramモデル**)

## Seq2Seq

文から他の分を生成するアーキテクチャ。

RNNをEncoder/Decoderに見かけて、データを入力、その情報をもとに系列データを出力する

### Reverse

エンコーダの入力分を反転させ、データを入力する

### Peeky(のぞき見)

エンコード結果を他の時系列の入力にも追加して渡す

実質的にskipConnectionのRNN版

## Attention

エンコーダの時系列的な隠れ層の出力を用いて、αで重みづけしてデコーダに渡すことで
どの時刻時の情報が主に文章に寄与しているかを渡せるようにした機構

ただエンコーダの隠れ層の出力を抽出して渡すだけでは逆伝搬できないため、
αで重みづけして渡す処理を加えることで逆伝搬できるように工夫されている。

αの取り方に*加法注意(Additive Attention)*と*内積注意(Dot-Production Attention)*がある

### Additive Attention

加法注意とも  

Attentionの重みaを求めるため、各エンコーダの隠れ状態全体と現在のエンコーダの隠れ状態をMLPに渡して、
重みを抽出するような計算を行う。

当然MLPがある都合上、パラメータは増えるし計算も複雑なので、余り使われない

### Dot-Product Attention

内積注意とも

Attentionの重みaを求めるため、各エンコーダの隠れ状態全体と現在のデコーダの隠れ状態にdotを使って内積を取る手法

### Self-Attention

1つの系列内(1文中)で各要素が他の要素にどのような関連があるかを見る

### Source Target Attention

Seq2Seqのように異なる系列間の各要素の類似度を算出する

### Attention付きbi-LSTM

そのままの意味。Attention機構を入れ込んだ双方向のLSTM

### Google Neural Machine Translation(GNMT)

Attention付きbi-LSTMにSkip-Connectionを入れて、更にGPUで並列処理可能にしたモデル

名前の通りGoogle開発

### Transformer

Attention機構のみをメインとして、単語の時系列的な情報は別の方法で学習させる形式にした新しい手法のモデル。
(LSTMが重すぎてGPUとかも有効活用できないので、変わりに時系列は別のベクトルとして扱い学習させる方式にした)

#### Positional Encoders

Transformerで時系列的な情報をLSTM経由せずに学習させるための工夫1

エンコーダに入れ込み学習する際、
単語の順序、位置関係をベクトル化して、元の埋め込みベクトルに付与する方法

#### Multi-Head Attention

並列的に複数のAttentionを計算、結合させる仕組みのこと

このままだと並列計算時に未来の情報もそのまま勝手に取ってAttentionを計算するので、
Transformerではそれを防ぐために「Masked Multi-Head Attention」と呼ばれる工夫を用いる
#### Masked Multi-Head Attention

Transformerで時系列的な情報をLSTM経由せずに学習させるための工夫2

デコーダにエンコーダの情報を入れ込む際、系列の後ろの要素（未来の情報）はマスクして隠すことで、
カンニング的に未来の情報を取ってくるような事をしないようにする工夫

### OpenAI GPT

一時期、「性能高すぎて悪用されそうだから公表できない」となった超精度の言語生成モデル

TransformerのEncorderを単語モデルに応用したアーキテクチャ。
GPT -> GPT-2 -> GPT-3と数字が増えるごとに大規模かつ膨大なパラメータでの学習が入っている。

### BERT

双方向にTransformerのEncoderを使ったモデル

GPTが単方向に対し、BERTは双方向となる
#### Maskerd Language Model(MLM)

文章の穴埋め問題を解くような形で学習を行う手法

#### Next Sentence Prediction(NSP)

2文から連続した文か不連続の文かを判定する手法。

これにより、会話がまだ続いているのか等を学習可能となる

### XLNet

MLMの工夫をし、実際のタスクを解くときにマスクによりノイズが出ていた部分を
予測単語の順序入れ替えなどで解決したモデル

### ALBERT

A Lite BERT

BERTを軽量化するためにWord Embedding(単語のベクトル化)にAuto Encoderの機構を入れたり、
各層のパラメータの重みを共有化させるなどをしてパラメータを削減、軽量化したモデル

### pronpt-based lerning

言語モデルを用いてプロンプト（適当な文）を生成することで
事前学習とFine-tuningのギャップを埋める学習法