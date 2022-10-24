def main(n,x):
    """
    Given a argument called 'n' and 'x' type of int , calculate the value of expression and return result:
    Args:
        n: int
        x: int
    Returns:
        result : int
    """
    answer=pow(x,n)+pow(n,x)
    return answer
print(main(3,6))
