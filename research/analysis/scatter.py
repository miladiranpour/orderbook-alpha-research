import matplotlib.pyplot as plt


def plot(

    feature,

    future,

    feature_name

):

    fig,ax=plt.subplots(

        figsize=(8,5)

    )

    ax.scatter(

        feature,

        future,

        s=5,

        alpha=.3

    )

    ax.set_title(

        feature_name

    )

    return fig