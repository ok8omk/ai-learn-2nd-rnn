import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tflearn

filename = 'international-airline-passengers.csv'

# データのグラフ描画
def draw_graph():
    dataframe = pd.read_csv(
            filename,
            engine = 'python',
            skipfooter = 3
        )
    ax = dataframe.plot()
    fig = ax.get_figure()
    fig.savefig('image.png')

# データ読み込み
def read_data():
    # ファイルの読み込み
    dataframe = pd.read_csv(
            filename,
            usecols = [1],
            engine = 'python',
            skipfooter = 3
        )
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    # データセットの正規化
    dataset -= np.min(np.abs(dataset))
    dataset /= np.max(np.abs(dataset))
    return dataset

# 読み込んだデータを入力データ教師データにしデータセットを生成
def create_dataset(dataset, steps_of_history, steps_in_future):
    X, Y = [], []
    for i in range(0, len(dataset)-steps_of_history, steps_in_future):
        X.append(dataset[i:i+steps_of_history])
        Y.append(dataset[i + steps_of_history])
    X = np.reshape(np.array(X), [-1, steps_of_history, 1])
    Y = np.reshape(np.array(Y), [-1, 1])
    return X, Y

# 訓練データとテストデータにデータセットを分割
def split_dataset(x, y, test_size=0.1):
    pos = round(len(x) * (1 - test_size))
    trainX, trainY = x[:pos], y[:pos]
    testX, testY   = x[pos:], y[pos:]
    return trainX, trainY, testX, testY

if __name__ == "__main__":
    # 前準備
    draw_graph()
    steps_of_history = 1
    steps_in_future = 1
    dataset = read_data()
    X, Y = create_dataset(dataset, steps_of_history, steps_in_future)
    trainX, trainY, testX, testY = split_dataset(X, Y, 0.33)
    # 実行
    # 入力層
    net = tflearn.input_data(shape=[None, steps_of_history, 1])
    # RNN層
    net = tflearn.simple_rnn(net, n_units=6)
    # 出力層
    net = tflearn.fully_connected(net, 1, activation='linear')
    # 学習法の設定
    net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
            loss='mean_square')
    # モデルの構築
    model = tflearn.DNN(net, tensorboard_verbose=0)
    # 学習
    model.fit(trainX, trainY, validation_set=0.1, batch_size=1, n_epoch=150)
