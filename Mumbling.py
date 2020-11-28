def accum(s):
    result = ''
    for x in range(len(s)):
        result += builder(s[x], x+1) + "-"
    return result[0:len(result)-1]

def builder(letter, num):
    length = len(letter)
    if (num == 1):
        return letter[0].capitalize() + letter[1:length]
    word = letter[0] + letter.lower()
    return builder(word, num - 1)