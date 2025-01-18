def modify(score: int, score2: int, score2_weight: float) -> float:
    """
    Modifies a normalized score by adding a second score with a given weight.
    Example: It'll adjust 'score' to fit 'score2' with a weight of 'score2_weight'.
    """

    return (score * (1 - score2_weight)) + (score2 * score2_weight)
