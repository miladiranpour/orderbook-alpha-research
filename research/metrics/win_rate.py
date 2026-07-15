import numpy as np


def calculate(feature, future):

    feature = np.asarray(feature)
    future = np.asarray(future)

    mask = feature > 0

    if mask.sum() == 0:
        return 0

    return (future[mask] > 0).mean()