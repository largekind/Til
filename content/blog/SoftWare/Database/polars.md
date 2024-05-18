---
title: "Polars"
date: 2024-05-18T18:58:25+09:00
---

# Polars

## 概要

Polarsは、高速なデータ処理を実現するためのDataFrameライブラリで、特にpandasを高速化したようなものとして着目されている
Rustで実装されており、マルチスレッド処理やメモリ効率が高いことが特徴

## インストール

```bash
pip install polars
```

## 基本的な使い方

### DataFrameの作成

```python
import polars as pl

# サンプルデータの作成
data = {
    "column1": [1, 2, 3],
    "column2": ["a", "b", "c"]
}

# DataFrameの作成
df = pl.DataFrame(data)
print(df)
```

### データの読み込みと書き出し

#### CSVファイルの読み込み

```python
df = pl.read_csv("sample.csv")
print(df)
```

#### CSVファイルの書き出し

```python
df.write_csv("output.csv")
```

### 基本的なデータ操作

#### 列の選択

```python
selected_df = df.select(["column1"])
print(selected_df)
```

#### フィルタリング

```python
filtered_df = df.filter(pl.col("column1") > 1)
print(filtered_df)
```

#### 集計

```python
agg_df = df.groupby("column2").agg(pl.col("column1").sum().alias("sum_column1"))
print(agg_df)
```

### 高速化のポイント

- **マルチスレッド処理**: Polarsは自動的にマルチスレッド処理を行い、計算を高速化
- **カラム指向のメモリレイアウト**: メモリ使用量を最小化し、効率的なアクセスを可能

## 比較: Polars vs. pandas

- **パフォーマンス**: Polarsは特に大規模データセットにおいてpandasよりも高速
- **メモリ効率**: Polarsはメモリ使用量が少なく、より効率的に動
- **APIの互換性**: pandasに似たAPIを提供しており、移行が比較的容易

## 参考リンク

- [Polars Documentation](https://pola-rs.github.io/polars-book/user-guide/)
- [GitHub Repository](https://github.com/pola-rs/polars)
