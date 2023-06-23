---
title: "PID Autotuning"
date: 2023-06-04T22:02:44+09:00
categories: ["Python"]
tags: ["Python", "PID", "utility"]
---
# PID Autotuning

## 概要

PIDによる簡単なオートチューニング方法を記載する

## 限界感度法

### 概要

Ziegler-Nichols法とも。

P制御のゲインと振動周期Tuを基準に、PIDのゲインを設定する方法。

詳細は次の[限界感度法の説明](https://controlabo.com/ultimate-sensitivity-method/)を参照

### サンプルコード

Pythonでの記述となる。

``` python

import math
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # 比例ゲイン
        self.ki = ki  # 積分ゲイン
        self.kd = kd  # 微分ゲイン
        self.error_integral = 0.0  # 誤差の積分値
        self.prev_error = 0.0  # 前回の誤差
        self.tu = 0.0  # 処理時間の目安

    def compute_control_signal(self, setpoint, feedback):
        error = setpoint - feedback  # 目標値と現在値の差分

        # PID制御の計算
        control_signal = self.kp * error + self.ki * self.error_integral + self.kd * (error - self.prev_error)

        # 積分値の更新
        self.error_integral += error

        # 前回の誤差の更新
        self.prev_error = error

        return control_signal

    def autotune_ziegler_nichols(self, setpoint, feedback):
        # オートチューニングの処理
        self.tu += 1.0  # 処理時間の目安を1.0単位で増加させる

        if self.tu >= 10.0:
            # 目安の処理時間が10.0以上になった時点でゲインを計算する
            ku = 4.0 / (self.tu * math.pi)
            self.kp = 0.6 * ku
            self.ki = 1.2 * ku / self.tu
            self.kd = 0.075 * ku * self.tu

    def get_tuned_gains(self):
        return self.kp, self.ki, self.kd


# 使用例
kp = 1.0  # 比例ゲイン
ki = 0.2  # 積分ゲイン
kd = 0.5  # 微分ゲイン
setpoint = 10.0  # 目標値

# 制御器の初期化
controller = PIDController(kp, ki, kd)

# フィードバック値の取得
feedback = 8.0

# 制御ループ
while abs(setpoint - feedback) > 0.01:  # 目標値に対する誤差が1%以内になるまでループする
    # オートチューニングの実行
    controller.autotune_ziegler_nichols(setpoint, feedback)

    # 制御信号の計算
    control_signal = controller.compute_control_signal(setpoint, feedback)

    # 制御信号の使用例
    # ここでは制御信号を出力する代わりに表示します
    print("Control Signal:", control_signal)
    print("Feed Back", feedback)

    # フィードバック値の更新（制御対象の出力など）
    feedback = update_feedback(feedback, control_signal)
```