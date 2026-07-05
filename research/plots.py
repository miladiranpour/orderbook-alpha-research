import matplotlib.pyplot as plt

def histogram(feature):

    plt.figure(figsize=(8,5))

    plt.hist(
        feature,
        bins=50
    )

    plt.title("Feature Histogram")

    plt.grid(True)

    plt.show()
    

def scatter(feature, future):

    n = min(len(feature), len(future))

    plt.figure(figsize=(8,5))

    plt.scatter(

        feature[:n],

        future[:n],

        s=5,

        alpha=0.25

    )

    plt.xlabel("Feature")

    plt.ylabel("Future Return")

    plt.grid(True)

    plt.show()
    

def average_return_plot(series):

    plt.figure(figsize=(9,4))

    series.plot.bar()

    plt.ylabel("Average Return")

    plt.grid(True)

    plt.show()
    
    
def probability_plot(series):

    plt.figure(figsize=(9,4))

    (series * 100).plot.bar()

    plt.ylabel("UP Probability (%)")

    plt.grid(True)

    plt.show()
    
    
