---
title: "AE"
date: 2023-04-06T00:00:00+09:00
lastmod: "2023-04-06"
---
# AE

## Auto Encoder

生成モデルの一種。EncoderとDeconderに分かれ、適当な入力に応じて何かしらを出力するモデル  
Encoder -> 潜在変数z -> Decoderの形でzに次元圧縮して何かしらの特徴に圧縮して、Decoderでその圧縮された特徴を用いてデータを出力する  

入ったものを圧縮してそのまま出すしかしてないので、**中間的な画像が出せないデメリットがある**

## Variational Autoencoder

通称VAE  
EncoderとDecoderの間にあるzを確率分布として平均、分散を求め、そこからサンプリングでzを取る形式になったもの  

確率変数をいじれば中間的な画像を連続的に出せる

損失関数は以下で与えられる

$$
L =  \underset{復元誤差}{\underline{E_{z \sim q(z|x)} \log_ P(x|z) }}-\underset{非負の正則化項}{\underline{D_{KL}(q(z|x)||P(z))}}
$$

- 復元誤差 : 入力と出力の差を小さくする項
- 非負の正則化項 : 潜在変数zの分布を入力モデルの分布に近づける

### Reparametrization Trick

VAEの学習で逆伝搬をするために、**ガウシアンノイズを用いてサンプリングを近似的に行うことで、逆伝搬可能にした方法**  
直訳すると「再パラメータ化トリック」というだけあって、サンプリングの処理をガウシアンノイズのパラメータで行うトリックを用いている

### posterior collpage

**VAEの問題** 表現力が高いDecoder(例:PixelCNN)などを用いると潜在変数が無視された生成が出てしまう  
対策として潜在変数zを離散的なベクトルに変えたVQ-VAEなどがある

## VQ-VAE

潜在変数に離散ベクトルを用いて学習させることで、上記の問題を解決させたVAE

## GAN

いつもの。Generative Adversal Network(敵生成ネットワーク)  
GeneratorとDiscriminatorを戦闘させて学習していくニセ札と警察の関係的な発想で生まれたネットワーク

