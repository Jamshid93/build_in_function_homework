def main(x,y):
    """
    Given a arguments called 'x' and 'y' type of int , calculate the value of expression and return result:
    Args:
        x: int
        y: int
    Returns:
        result : int
    """
    answer=(pow(x,2)+6*pow(x,3)+3*x*y)
    return answer
print(main(5,2))