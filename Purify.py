def purify(items):
    newList = list()
    for item in items:
        if item % 2 == 0:
            newList.append(item)
    return newList
