def in_array(array1, array2):
    newList = []
    for i in array1:
        for item in array2:
            if i in item and i not in newList:
                newList.append(i)
    return sorted(newList)