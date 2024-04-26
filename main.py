import chess
from Constants import valueTable
from randomBoard import stockfish, random_board
from processingNeural import split_dims
import tensorflow as tf
import threading
import pickle
from stockfish import Stockfish


board = chess.Board()
processedDataSet = []
i = 0


def generate_dataset():
    currentboard = stockfish(random_board())
    if currentboard["type"] != "none":
        currentboard["board"] = split_dims(currentboard["board"])
        processedDataSet.append(currentboard)
        print(len(processedDataSet))


def build_model(conv_size, conv_depth):
    board3d = tf.keras.layers.Input(shape=(14, 8, 8))
    x = board3d
    for _ in range(conv_depth):
        x = tf.keras.layers.Conv2D(filters=conv_size, kernel_size=3,
                                   padding='same', activation='relu')(x)
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(64, 'relu')(x)
    x = tf.keras.layers.Dense(1, 'sigmoid')(x)
    return tf.keras.models.Model(inputs=board3d, outputs=x)


while len(processedDataSet) < 1048576:
    threading.Thread(target=generate_dataset, name='thread {}'.format(i)).start()


# Code to write to a file
with open('dataSet', 'ba') as fp:
    pickle.dump(processedDataSet, fp)


# Code to read a file
with open('dataSet', 'rb') as fp:
    itemList = pickle.load(fp)
    print(itemList)