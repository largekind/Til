---
title: "強化学習"
date: 2023-04-05T00:00:00+09:00
tags: ["Python", "AI"]
categories: ["AI"]
---
# 強化学習

## 教師あり学習

正解がわかっているデータをもとに、入力データと対応する正解の出力の関係を学習する  
画像分類などが該当

## 教師なし学習

与えられたデータが持つ構造そのものを学習。正解そのものが無い  
SVMやクラスタリングが該当
## 強化学習

**報酬**をもとに、最適な意思決定を作成するための学習方法  
五目並べとか遺伝子的アルゴリズムとかが該当

## マルコフ決定過程

「状態」 + 「行動」+ 「報酬」で最適化を行う処理  
確率的に変化させる決定に報酬や行動によるウェイトを追加したもの

### マルコフ過程

「状態」で一意に決まる確率過程のこと  
数学者であるアンドレイ・マルコフにちなんで命名された  
これに「行動」と「報酬」が入るとマルコフ決定過程になる
### マルコフ性

今の状態に応じて次の状態が決定するという性質。  
*今*が次を決めるやつ。過去の自分に影響されたり、未来からドラ〇もんが来て状態が勝手に変化するとかは無いよっていうやつ

## 方策

どう行動を決定するかを考えるための決まりや戦略の基準となる部分。

### 割引率

**未来に対する報酬に対する影響に対して重みづけを行うための報酬のウェイト値**  
直近だけでなく、未来の報酬もある程度考慮して考えるための影響度の度合い

### 累積報酬和

価値を表す総和の式。  
R = 直近の報酬 + 次の報酬 * 割引率 + さらに次の報酬 * 割引率^2 + ... = 報酬*時間分の割引率の総和

上を価値関数として見て、最大化するのが目的となる


### 価値関数

強化学習における目的関数のこと  
実質的に累積報酬和をmaxへ持っていくための行動と状態を表す式が価値関数になる

### 最適ベルマン方程式

*「今の価値」* + **今後の価値の期待値**で決まる価値関数  
「価値を最大化する行動」 = 「価値を最大かする最適な方策」を結びつけることが出来る

## 強化学習におけるアプローチ

### 価値関数ベース

価値を最大化するような行動をする（最適な行動をする）のを軸に評価するアプローチ  
**価値そのものをモデル化**して、行動自体は別のアルゴリズムに代用させる形式

### 方策ベース

価値を最大するような行動ルール(方策)を見つけようとするのを軸に評価するアプローチ  
**方策（行動の選択方法）をモデル化**する方式

## 価値関数ベースのアプローチ

### 行動価値関数(Q)

一定の条件時での価値関数の値を求める関数。  
ある状態である状態を取ったときの価値に限定した方法

### 価値関数法

価値関数をもとに行動を選択、試行を繰り返して価値関数を更新する手法  
**環境に対する知識(環境ダイナミクス)が完璧にある時に使用できる**

#### 環境ダイナミクス

状態転移確率と報酬が既知である状態  
迷路とか完璧に設計されているような、既に分かっている問題などが該当

### 環境のサンプリング

**実際に行動してみて、その得た情報で価値関数を更新する方式**  
とりあえずやってみよう理論

#### モンテカルロ法

最後までプレイして、その報酬から価値を推定する方式  

更新式は以下の以下の通り
$$
\begin{align}
V(S_t) \leftarrow V(S_t) + \alpha [R_t - V(S_t)]\\
Q(S_t,a_t) \leftarrow Q(S_t,a_t) + \alpha [R_t - Q(S_t,a_t)]
\end{align}
$$

一連の行動をやった後に累積報酬和$R_t$から価値関数を推定する方式となる。

そのため、即時報酬$r_t$や割引率$\gamma$などはない


#### TD法(Temporal Difference Learning)

その時までに得た報酬で価値関数を更新する手法  
(即時報酬で更新していく)

具体的には「１つ先の報酬とその行動価値」と「現在の行動価値」との差を用いて、最適な行動価値関数へ更新していく手法。
このアイデアをアルゴリズム化したのがQ学習になる。

その時までに得た報酬で更新する関係で、初期に得た価値が学習されづらいデメリットがある

### 局所解への対策

強化学習は初期の方策（行動）に依存しやすい傾向があるため、  
たまには今までの学習を無視して行動させようという対策がある

#### ε-greedy方策

確率εでランダム行動させる方策

#### ソフトマックス方策

ある程度の今までの学習を用いて、ボルツマン分布に従い行動を設定させる  
（完全ランダムではなく、ある程度今までの学習も信用してランダムな行動をする）

## TD法の分類
### Q学習

**方策OFF型**  
次の状態がどれくらいの価値を持つかを*現在推定されている値のMax*を用いてQ値を更新する手法  
「明日は自分はベストな行動取るだろう」と信じて学習していく手法  
最適なベスト値(Max値)を取っているので学習が安定する。

**SARASAよりも収束が早いメリットもある**

### SARASA

**方策OFF型**  
今の方策に従って値を更新していく手法  
「未来より、今の自分を信じる」として学習していく手法  
現在の方策で得た値を取る(ランダム性がある)ため学習が若干不安定だが、局所解に陥る危険が少ない


## 方策勾配法(方策ベース)

土の手をどれくらいの確率で選択すべきかの**方策**自体を直接予測  
**未来の盤面を列挙しない** + 相性の良い手法と組み合わせて、性能が良い方策を実現可能！

### 方策勾配定理

方策パラメータΘに対する偏微分で得られる方策勾配が満たす性質のこと  
**行動価値関数のQ値が分かればベストな方策がわかるよ定理**  

価値関数をΘで偏微分するメチャクチャ面倒な式なので覚えたほうが早い  
*デメリットとしてQ値を求めるのが難しいので、Q値の平均値などを工夫して必要がある*

#### ベースライン関数

現在の報酬からベース分引いて、分散を抑えるための関数

#### アドバンテージ関数

行動価値関数から推定される価値関数を引くことで、ある程度の分散を抑える関数


## 方策ベースのアプローチ

### REINFORCEアルゴリズム

REINFORCE : 強化  
実際に得られた報酬の平均を使って近似したものをQ値とする方法  
「死ぬたびに学習→強くなる」方式

### Actor Critic

Actor Critic : 演者 - 評論家  
状態価値をNeaural Networkを用いて推測させ、方策を決定させる方式  
「演者が上手く演技しているか、評論家が評価して強くしていく」方式

### A3C

Asynchoronous advantage Actor Crinic の略  
Actor Crinicに加えて、パラメータの更新を非同期で行う*Asynchrouns*と推定にAdvantageを用いる形式  
(Asynchoorus + Advantage + Actor : A3)  
「演者がどれだけ有利に事を運んで演技しているかを、評論家が一度にいっぱい見ながら評価して強くしていく」方式

#### A2C

A3Cの同期分散処理版モデル  
Asynchorousが消えているのでA2C  
**同期するのでGPUで使いやすいメリットがある**


#### ACER

A3Cベースに勾配オフ型にし、Experience Replay(経験再生)を利用したモデル  
過去の履歴も学習できるようになり、更に収束しづらい問題は*Retrace*と呼ばれる手法で解決している

#### UNREAL

Unsupervied reinforcement and auxiliary learning : 教師なしでの補助学習  
A3Cベースに補助タスクも同時学習させたモデル  
「色んな学習を同時に強化学習させよう」モデル