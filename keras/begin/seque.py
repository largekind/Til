from keras.models import Sequential
from keras.layers import Dense,Activation

# レイヤーを設定 Dense->全結合レイヤー
model = Sequential([
    # 1層目 -> 個数32 次元が784 のレイヤー
    Dense(32,input_shape=(784,)),
    # relu関数で活性化
    Activation('relu'), 
    # 2層目 -> 数10のレイヤー
    Dense(10),
    # ソフトマックス関数で活性化
    Activation('softmax')
])

