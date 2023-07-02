def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list1=[1, 0, 1, 1, 0]
    n = 0
    while n < len(list1):
        if list1[n] == 1:
            list1[n] = True
        n += 1
    return list1
print(main(list1=[1, 0, 1, 1, 0]))