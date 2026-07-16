import pandas as pd

from research.ranking.engine import build_ranking



def main():

    metrics_df = pd.DataFrame({

        "Feature":[
            "Imbalance",
            "Weighted Imbalance",
            "Queue Imbalance",
            "Microprice",
            "Book Pressure",
            "OFI"
        ],


        "Correlation":[
            0.180904,
            0.183554,
            0.182941,
            0.006610,
            0.188537,
            0.092849
        ],


        "Average Return":[
            0.000053,
            0.000055,
            0.000056,
            0.000056,
            0.000053,
            0.000032
        ],


        "Win Rate":[
            0.553897,
            0.556250,
            0.556678,
            0.556678,
            0.553897,
            0.525465
        ],


        "Sharpe":[
            0.166531,
            0.173330,
            0.175445,
            0.175445,
            0.166531,
            0.099360
        ]

    })


    ranking = build_ranking(

        metrics_df

    )


    print("\n========== RANKING ==========\n")

    print(ranking)


    print("\n========== CHECKS ==========\n")


    print(

        "Sorted:",

        ranking["Score"].is_monotonic_decreasing

    )


    print(

        "Has NaN:",

        ranking.isnull().sum().sum()

    )


    print(

        "Ranks:",

        ranking["Rank"].tolist()

    )



if __name__ == "__main__":

    main()