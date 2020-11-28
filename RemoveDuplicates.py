def remove_duplicates(liste):
    newList = list()
    for item in liste:
        if item not in newList:
            newList.append(item)
    return newList
