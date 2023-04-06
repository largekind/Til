---
title: "GRU"
date: 2023-04-05T00:00:00+09:00
---
# GRU

LSTMを簡略化、リセットゲートと更新ゲートのみで時系列を処理できるようにしたやつ

## 順伝搬の実装

``` python
class GRU:
    def __init__(self, Wx, Wh , b):
        # Wx : 入力用の重みパラメータ
        # Wh : 隠れ状態h用の重みパラメータ
        # b :バイアス
        self.params = [Wx, Wh]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None

    def forward(self, x, h_prev):
        Wx, Wh , b = self.params
        N, H = h_prev.shape
        Wxz, Wxr, Wx = Wx[:, :H], Wx[:, H:2 * H], Wx[:, 2 * H:]
        Whz, Whr, Wh = Wh[:, :H], Wh[:, H:2 * H], Wh[:, 2 * H:]

        # z : 更新ゲートの出力
        z = sigmoid(np.dot(x, Wxz) + np.dot(h_prev, Whz))
        # r : リセットゲートの出力
        r = sigmoid(np.dot(x, Wxr) + np.dot(h_prev, Whr))
        # h_hat : tanhを過ぎた直後の隠れ層の出力
        h_hat = np.tanh(np.dot(x, Wx) + np.dot(r*h_prev, Wh))
        # h_next : 次の隠れ層の出力 h_prevとzの積および (1-z)とh_hatの積を足したものになる
        h_next = z*h_prev + (1 - z) * h_hat

        self.cache = (x, h_prev, z, r, h_hat)

        return h_next


```
