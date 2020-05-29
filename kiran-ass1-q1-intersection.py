def get_intersection(x, y, u, v):
    """
    The new interval [a, b] will be such that a = max(x, u), i.e., the higher
    of the starting points and b = min(y, v), i.e., the smaller of the two
    boundaries. Draw the two intervals on a number line to visualize.
    """
    return {max(x, u), min(y, v)}
