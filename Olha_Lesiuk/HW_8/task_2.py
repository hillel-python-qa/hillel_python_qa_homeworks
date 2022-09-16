"""
    Implementing my own filter function.
    """


def my_own_filter(callback: callable, sequence: iter):
    return [item for item in sequence if callback(item)]
