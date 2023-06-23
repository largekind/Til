---
title: "GAN"
date: 2023-04-05T00:00:00+09:00
tags: ["Python", "AI", "GAN"]
categories: ["AI"]
---
# GAN

敵対的生成ネットワーク。まぁ詳しい情報はGoogle

2016年から一気にいろいろなGANが増えている

## noize to imgのGAN

ノイズから画像を生成する一般的なGANの紹介

### LAPGAN (2015)

Laplacian pyramid GAN

低解像度の画像をまず生成して、そこから少し高解像度の画像を生成、さらに...といった流れで繰り返して最終的に高い高解像度の画像を生成する手法

小さい解像度 -> 解像度+1 -> ... -> 解像度+高 といったピラミッド的な流れで進んでいく

### DCGAN (2015)

Deep Convolutional GAN

名前の通り、CNN版GAN。超有名なのであまり説明することがない...

Generatorは通常のConv、DiscriminatorにはdeConvを使ってる

#### Leakly Relu

DCGAN Discriminatorの学習で使われている活性化関数。
Reluの負値にもある程度傾斜をつけたRelu改良版。

通常のReluだとGeneratorまでに逆伝搬させる際、0以下の情報が伝搬せず学習が上手くできない問題があったためにLeakly Reluにした模様。

### PGGAN

Progressive Growing GAN

低解像度画像から徐々にレイヤーを追加、解像度を上げていくGAN

まさしく、レイヤーをピラミッド状に積み重ねていって学習するGAN

当然、レイヤー追加 = 高解像度化するたびにGANを変えていくので、アホみたいに計算量とメモリを食べる

### SinGAN

単一画像を高解像度化するように学習するやつ。

高解像度の入力画像に対して、ダウンスケール + ノイズを加えて訓練データとして学習、元画像と一致するように学習してくことで、
その後の超解像タスクや他アニメーションタスクなどの補完が可能なようにする。

#### reconstruction loss

SinGANに使われているLoss。

通常のGANの損失関数に加えて、「生成画像と入力した画像が離れないようにする」ためのLossを付与して損失とする

画像の離れ具合は**penalty coefficient**を指定して対応する。大きいほど多様性がある画像となる。

#### WGAN-gp

Wasserstein距離 + gradient penarityで作られたDiscriminator用損失関数。

「本物画像と入力画像のWasserstein距離」にgradient perarityと呼ばれるものを追加してある程度Discriminatorの学習を易化したもの


## クラス指定画像生成

通常のGANで使われている入力のノイズに加え、クラスも情報として入力することで、特定の画像を指定・出力可能になったGAN

### CGAN (Conditional GAN)

データセットのクラス情報も入力に与えることで、クラスの分類、精度upしたGAN

### InfoGAN (2016)

潜在変数を用いて、いろいろな変化をラベル付けなしで獲得できるようにしたGAN


### ACGAN (2016)

InfoGANに加えて、Discriminatorにクラス分類を追加、高精度な画像を出せるようにしたやつ

### SAGAN (2018)

Self-Attentionを入れることでConv層が局所的なものしか着目できない問題を解決、
大域的な関係性を見れるようにしたGAN

### BigGAN(2018)

でかいGAN。Truncated Trickと呼ばれる手法で出力画像の多様性と画質をトレードオフで調節できるようにしたGAN

Bigのため学習コストがやばい

### StyleGAN(2018)

Styleと呼ばれる情報を渡すことで、その特徴が入り込んだ画像を生成可能なGAN

スタイルを各層に取り込むためにAdaINと呼ばれる仕組みがある

#### AdaIN

Adaptive Instance Normalization

正規化したコンテンツ入力をスタイル入力にシフトさせる手法

計算式は以下の通り
$$
AdaIN(x,y) = y_{s,i}\frac{x_i - \mu(x_i)}{\sigma (x_i)} + y_{b,i}
$$

## img -> imgのGAN(画像変換)

画像のスタイル変換や加工などを行うGAN

### pix2pix

画像間の関係性を考慮して学習することで、「画像 -> カラー」といった変換を可能にしたGAN

画像間の関係を出すため、きちんと対応付けされたペア画像を用意する必要がある難点がある

### Cycle GAN (2017)

馬 - シマウマみたいに画像のドメインを返還するGAN。

方法例として「馬-シマウマ」であれば、最初に「ウマ -> シマウマ」用Generatorで何かしらのウマ画像を渡し、
シマウマに生成された画像を「シマウマ -> ウマ」用のGeneratorに渡して、元のウマ画像に戻るように学習を行う

ペア画像を用意しなくても、対象の画像を大量にあつめることで包括的な特徴をとってきて変換可能になるGAN
### StarGAN (2017)

Cycle GANではA - Bと一対一でしか変換できないのを、複数の変換が可能な形にCycle GANを改良したもの

## その他 GAN

### Stack GAN

テキストから画像生成するGAN

CGANのクラス部分をテキストにし、GANを2段構造にしたアーキテクチャ。
(１段目でそれっぽい粗画像を作り、そこから高精度化するGANに渡す)

### Ano GAN

Anomary Detection with GAN

異常検知用のGAN。入力画像にできるだけ近い画像を生成するGAN