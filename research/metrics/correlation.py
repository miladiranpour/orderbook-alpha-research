import numpy as np


def calculate(feature, future):

    feature = np.asarray(feature)
    future = np.asarray(future)

    return np.corrcoef(feature, future)[0, 1]