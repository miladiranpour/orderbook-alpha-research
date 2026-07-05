def build_labels(future_returns):

    labels = []

    for ret in future_returns:

        if ret > 0:
            labels.append(1)
        else:
            labels.append(0)

    return labels