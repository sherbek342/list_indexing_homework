def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    n = 0
    result = list_num[0]
    while n < len(list_num):
        if result < list_num[n]:
            result = list_num[n]
        n += 1
    return result
print(main(list_num=[12, 2, 5, 22, 7, 9, 1]))