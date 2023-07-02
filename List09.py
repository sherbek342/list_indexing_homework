def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    n = 0
    m = 0
    result = ''
    while n < len(list1):
        if list1[0]==list1[n]:
            m = m +1
        if len(list1) == m:
            result = True
        else:
            result = False
    
        n += 1
    return result
print(main(list1=[1, 1, 1, 1, 1]))