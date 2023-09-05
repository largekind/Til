---
title: "基本的なAIモデルの処理作成の流れ"
date: 2023-08-27T22:12:02+09:00
categories: ["Python"]
tags: ["Python", "pytorch"]
---
# 基本的なAIモデルの処理作成の流れ

## 概要

毎回忘れてしまう、pytorchを用いた基本的なAI処理（画像分類）の作成の流れを列挙する

基本的には以下の流れである
1. データセットを定義
2. modelの定義
3. 学習処理の作成
4. 推論処理の作成

## データセットの定義

当然、学習するにはデータセットが必要なため、その定義方法を簡単にまとめる

構造が以下のようにクラスがディレクトリで分類されている場合はImageFolderで適用可能
``` tree
train
├─A
├─B
├─C
└─D
```

``` python
dataset = datasets.ImageFolder('Path')
```

その後、以下のようにデータ分割 今回であればtrain/val/testを0.7/0.15/0.15にした場合、以下のような感じ
``` python
# 訓練データ、検証データ、テストデータに分割
num_data = len(dataset)
train_size = int(0.7 * num_data)
val_size = int(0.15 * num_data)
test_size = num_data - train_size - val_size

train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

# データローダの作成
train_loader = DataLoader(train_dataset, batch_size=batch_size)
val_loader = DataLoader(val_dataset, batch_size=batch_size)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

```

### Tips : WeightedRandomSampler

クラスなどが傾いている状態（極端に特定のクラスの写真が少ないなど）がある場合、上手くその情報が学習できない場合がある。

そういった状況の時に、学習時の割り当てされる確率を操作することで特定のクラスの学習をよくする手法としてpytorchに提供されている

使い方は以下のコードの通りである

``` python
# 各クラスのデータポイントに適用する重みを計算
num_samples = sum(class_counts.values())
class_weights = {cls: num_samples / count for cls, count in class_counts.items()}

# すべてのデータポイントに対する重みのリストを作成
sample_weights = [class_weights[dataset.classes[label]] for _, label in train_dataset]

# WeightedRandomSamplerを作成
sampler = WeightedRandomSampler(weights=sample_weights, num_samples=len(sample_weights), replacement=True)

# DataLoaderの設定
train_loader = DataLoader(train_dataset, batch_size=batch_size, sampler=sampler)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
```

上記samplerで定義することで、特定のクラスの重みづけを行うことが可能。
ただし、samplerを用いた場合shuffleはできないので注意

## モデルの作成

学習させるためのモデルを作成していく。

よほどの理由がない限りは既存のモデルを流用し、出力層だけ変えれば良いはず

``` python
# モデルの定義
model = efficientnet_b5(pretrained=True)
# 最終層を取得
num_ftrs = model.classifier[1].in_features
# 出力層を置き換え
model.classifier[1] = nn.Sequential(
    nn.Linear(num_ftrs, 4), # 4クラス分類のための出力層を追加
    nn.Dropout(0.5),       # 50%の確率でドロップアウトを適用
)  
```

## 学習用コードの作成

学習を行うためのコードを作成する
以下一例

``` python

# 訓練処理
def train_model(train_loader, val_loader, num_epochs=100, patience=5):
    """ 
    Parameters:
    - train_loader: 訓練データのデータローダ
    - val_loader: 検証データのデータローダ
    - num_epochs: エポック数
    
    Returns:
    - model: 訓練されたモデル
    """
    # モデルの定義
    model = Model
    model = model.to(device)
    
   # 損失関数と最適化手法の定義
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.0005, weight_decay=1e-5)
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
    
    # early stopping用の値
    best_val_loss = float('inf')
    epochs_without_improvement = 0
    
    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        
        # 訓練フェーズ
        for inputs, labels in tqdm(train_loader, desc=f"Epoch {epoch + 1}/{num_epochs} - Training"):
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)
        
        train_loss = running_loss / len(train_loader.dataset)
        
        # 検証フェーズ
        model.eval()
        running_loss = 0.0
        all_preds = []
        all_labels = []
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            with torch.no_grad():
                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)
                loss = criterion(outputs, labels)
                running_loss += loss.item() * inputs.size(0)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())
        
        val_loss = running_loss / len(val_loader.dataset)
        f1 = f1_score(all_labels, all_preds, average='weighted')
        
        print(f"Epoch {epoch + 1}/{num_epochs} - Training loss: {train_loss:.4f}")
        print(f"Epoch {epoch + 1}/{num_epochs} - Validation loss: {val_loss:.4f}, Validation F1-score: {f1:.4f}")
        
        # 学習率の更新
        scheduler.step()
        
        # Early stoppingの判定
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_without_improvement = 0
        else:
            epochs_without_improvement += 1
            if epochs_without_improvement >= patience:
                print(f"Early stopping after {epoch + 1} epochs!")
                break
    
    return model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
```