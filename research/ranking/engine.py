def build_ranking(metrics):
    """Rank feature results by descending correlation."""
    ranking = metrics.copy()

    if ranking.empty:
        ranking["Rank"] = []
        return ranking

    ranking = ranking.sort_values(by="Correlation", ascending=False)
    ranking["Rank"] = range(1, len(ranking) + 1)

    return ranking
