def top_n(items, n):
    """
    Return the top n items in an array
    Args:
        items (array): list of items
        n (int): number of top items to return
    Returns:
        array: list of top n items in desc order

    Egs:
        >> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):

            if items[j] > items[j + 1]:  # if this item is bigger than the next item..
                items[j], items[j + 1] = items[j + 1], items[j]  # swap the two items

    # get the last two items
    top_n = items[-n:]

    # retun in descending order
    return top_n[::-1]
