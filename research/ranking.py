import pandas as pd


def build(df):

    df=df.sort_values(

        by="Correlation",

        ascending=False

    )

    df["Rank"]=range(

        1,

        len(df)+1

    )

    return df