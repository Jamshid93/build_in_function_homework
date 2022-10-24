def main(n):
    """
    Given a argument called 'n' type of int , calculate the value of expression and return result:
    Args:
        n: int
    Returns:
        result : float
    """
    n=pow(((2+n)/3),2)
    return n
print(main(4))