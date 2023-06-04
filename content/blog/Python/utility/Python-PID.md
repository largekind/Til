---
title: "Python上での簡単なPID制御"
date: 2023-06-04T21:45:00+09:00
categories : ["Python"]
tags : ["Python","utility"]
draft: true
---

# Python上での簡単なPID制御

## 概要

Pythonでの簡単なPID制御の仕組みを作成する

サンプルコードのため、他プログラムなどに考えが流用できるはず

## PIDとは

[次のPID制御を参照](content\blog\InfoEngineer\Software\PID.md)

## 通常のPID制御サンプル

``` python
# PIDの簡単な処理クラス
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp  # 比例ゲイン
        self.ki = ki  # 積分ゲイン
        self.kd = kd  # 微分ゲイン
        self.error_integral = 0.0  # 誤差の積分値
        self.prev_error = 0.0  # 前回の誤差

    def compute_control_signal(self, setpoint, feedback):
        error = setpoint - feedback  # 目標値と現在値の差分

        # PID制御の計算
        control_signal = self.kp * error + self.ki * self.error_integral + self.kd * (error - self.prev_error)

        # 積分値の更新
        self.error_integral += error

        # 前回の誤差の更新
        self.prev_error = error

        return control_signal

# 仮想的な制御対象の更新関数
def update_feedback(feedback , control_signal):
    # ここに制御対象の出力を更新する処理を実装する
    # 例えば、制御対象が温度制御の場合は温度を計測し、制御信号を入力して温度を更新する処理などを記述する
    # この例では、制御信号を加えた場合にフィードバック値が変化すると仮定し、feedbackに加算する
    feedback += control_signal
    return feedback
    
# 使用例
kp = 1.0  # 比例ゲイン
ki = 0.2  # 積分ゲイン
kd = 0.5  # 微分ゲイン
setpoint = 10.0  # 目標値

# 制御器の初期化
controller = PIDController(kp, ki, kd)

# フィードバック値の取得（ループ内で更新される想定）
feedback = 8.0

# 制御ループ
while abs(setpoint - feedback) > 0.01:  # 目標値に対する誤差が1%以内になるまでループする
    # 制御信号の計算
    control_signal = controller.compute_control_signal(setpoint, feedback)

    # 制御信号の使用例
    # ここでは制御信号を出力する代わりに表示します
    print("Control Signal:", control_signal)
    print("Feed Back", feedback)

    # フィードバック値の更新（制御対象の出力など）
    feedback = update_feedback(feedback ,control_signal)
```

ただし、この方法ではゲインを手動で調整する必要がある。
