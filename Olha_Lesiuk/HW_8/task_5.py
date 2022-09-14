def my_all(x: list) -> bool:
    """
        Implementing my all function.
        """
    for element in x:
        if not element:
            return False
    return True
