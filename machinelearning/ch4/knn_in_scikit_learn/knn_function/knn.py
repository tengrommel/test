import numpy as np
from math import sqrt
from collections import Counter


def knn_classify(k, x_train, y_train, x):
    assert 1 <= k <= x_train.shape[0], "k must be valid"
    assert x_train.shape[0] == y_train.shape[0], "the size of x_train must equal to the size of y_train"
    assert x_train.shape[1] == x.shape[0], "the feature number of x must be equal to X_train"
    distances = [sqrt(np.sum((x_t - x)**2)) for x_t in x_train]
    nearest = np.argsort(distances)
    topK_y = [y_train[i] for i in nearest[:k]]
    votes = Counter(topK_y)
    return votes.most_common(1)[0][0]
