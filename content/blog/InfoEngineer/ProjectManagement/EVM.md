---
title: "EVM : Earned Value management"
date: 2023-04-05T00:00:00+09:00
tags: ["InfoEngineer", "ProjectManagement"]
categories: ["InfoEngineer"]
---
# EVM : Earned Value management

Earned Value : 出来高

**コスト**と**スケジュール**の２つを定量的に管理する進捗管理手法

主に以下3つが存在
- PV(Planned Value) : 予想(計画)していた成果価値
- EV(Earned Value) : 実際の成果価値
- AC(Earned Cost) : 実際のコスト

上記3つの指標からさらに以下の計算が取れる
- CV(Cost Variance) : コスト差異
  - $EV-AC$、つまり実際の成果価値から実際のコストの差で求められる
  - プラスなら予算内、マイナスなら予算オーバとなる
- SV(Schedule Variance) : スケジュール差異
  - $EV-PV$、つまり実際の成果価値から予想価値の差で求められる
  - プラスならスケジュール通り(or早い)、マイナスなら遅延となる
- CPI(Cost Performance Index) : コスト効率指標
  - 特定の時点でコストがどれくらい発生しているのかを表す指標
  - $EV/AC$ 、つまりは実際の成果価値とコストの割合で表す
  - 1以上ならコストが抑えられており、1以下ならコストが高いと見れる
- SPI(Schedule Performance Index) : スケジュール効率指標
  - 特定の時点でスケジュールが計画的に動いてるのかを示す指標
  - $EV/PV$、つまり実際の成果価値と予定していた価値の割合で示す
  - 1以上なら計画通り、1以下なら遅延していることを示す

上記に加え、BACと呼ばれる以下の指標もある
- BAC(Buddet At Completion) : プロジェクト完了までに必要な総予算
BACも加えた場合、以下の指標も計算可能となる
- ETC(Estimate To Complete)
  - 残作業コスト予測 つまり今後の作業工数を金銭換算したもの
  - $(BAC - EV)/ CPI$で求められる
- EAC(Estimate At Completion)
  - 完成時のコスト見積もりを指す
  - $BAC / CPI$で求められる
- VAC(Variance At Completion)
  - 完了時のコスト差異を指す
  - $BAC - EAC$で求められる