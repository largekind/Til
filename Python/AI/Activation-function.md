# 活性化関数まとめ

## ステップ関数

階段関数とも。最適化が難しいため余り使用されない。

$$

{y = \left\{
  \begin{array}{cc}
    1 & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}

$$

## ReLU

中間層における最適化で高い精度を誇る。

基本的に色んなNNで使用される認識。

- 順伝搬
$$ 
{y = \left\{
  \begin{array}{cc}
    x & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}
$$
- 逆伝搬
$$
{y = \left\{
  \begin{array}{cc}
    1 & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}
$$
