def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    answer=2*(pow(y,3)+pow(x,2)*y)
    return answer
print(main(2,4))

