def reverse(text):
    counter = len(text)
    inverse = ""
    while(counter > 0):
        inverse += text[counter-1]
        counter -= 1
    return inverse
