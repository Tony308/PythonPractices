def count(sequence, item):
    counter = 0;
    for stuff in sequence:
        if item == stuff:
            counter += 1
    return counter
