def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    number1 = list_num[0]
    number2 = list_num[-1]
    max = 0
    if number1 > number2:
        max += number1
    else:
        max += number2

    return max