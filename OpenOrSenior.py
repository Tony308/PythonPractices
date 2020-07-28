def open_or_senior(data):
    result = []
    for arr in data:
        print(arr)
        age = arr[0]
        handicap = arr[1]
        if age > 54 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")

    return result