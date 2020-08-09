import torch
import tensorflow as tf

if __name__ == '__main__':
    print("torch GPU:", torch.cuda.is_available())
    print("tensorflow gpu:", tf.config.list_physical_devices('GPU'))
