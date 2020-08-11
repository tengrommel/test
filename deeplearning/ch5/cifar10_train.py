import tensorflow as tf
from tensorflow.keras import layers, optimizers, datasets, Sequential
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
tf.random.set_seed(2345)

conv_layers = [
    # unit 1 两个卷积层
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 2 两个卷积层
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 3 两个卷积层
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3,3], padding="same", activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),
]


def main():
    conv_net = Sequential([conv_layers])
    conv_net.build(input_shape=[None, 32, 32, 3])
    x = tf.random.normal([4, 32, 32, 3])
    out = conv_net(x)
    print(out.shape)


if __name__ == '__main__':
    main()