def mapper(func, *sequences):
    """
        Implementing my own map function.
        """

    result = []
    if len(sequences) > 0:
        min_l = min(len(subseq) for subseq in sequences)
        for i in range(min_l):
            result.append(func(*[subseq[i] for subseq in sequences]))
    return result
