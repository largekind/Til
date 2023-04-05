---
title: "Wassertein GAN"
date: 2023-04-06T00:00:00+09:00
lastmod: "2023-04-06"
---
# Wassertein GAN

通常のGANがJSD(Jensen–Shannon divergence : イェンセン・シャノン情報量)を使うのに対し、

確率密度関数の距離を測る**Earth Mover's Distance（Wasserstein distance）**を用いて学習、勾配消失を解決したGAN

**EarthEarth Mover's Distance = Wasserstein distanceと同じなので注意**
**EM GANという名はなく、Wassertein GANになる**