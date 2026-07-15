import matplotlib.pyplot as plt


def plot(

    feature,

    feature_name

):

    fig,ax=plt.subplots(

        figsize=(8,5)

    )

    ax.hist(

        feature,

        bins=50

    )

    ax.set_title(

        feature_name

    )

    return fig