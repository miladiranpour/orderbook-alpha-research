from research.metrics import METRICS

from .normalize import normalize
from .scorer import score


def build_ranking(

    metrics_df

):

    normalized = normalize(

        metrics_df,

        METRICS

    )

    scored = score(

        normalized,

        METRICS

    )

    ranking = scored.sort_values(

        by="Score",

        ascending=False

    ).reset_index(

        drop=True

    )

    ranking.insert(

        0,

        "Rank",

        range(

            1,

            len(ranking)+1

        )

    )

    return ranking