import numpy as np


def correlation(feature, future_return):

    feature = np.array(feature)

    future_return = np.array(future_return)

    return np.corrcoef(
        feature,
        future_return
    )[0,1]
    
    
def average_return(feature, future_return):

    feature = np.array(feature)

    future_return = np.array(future_return)

    mask = feature > 0

    return future_return[mask].mean()

def win_rate(feature, future_return):

    feature = np.array(feature)

    future_return = np.array(future_return)

    mask = feature > 0

    return np.mean(
        future_return[mask] > 0
    )
    
def sharpe(feature, future_return):

    feature = np.array(feature)

    future_return = np.array(future_return)

    mask = feature > 0

    r = future_return[mask]

    return r.mean() / r.std()