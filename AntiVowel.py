#!/usr/bin/env python
def anti_vowel(text):
    vowels = ['a','e','i','o','u', 'A', 'E', 'I' ,'O', 'U']
    word = ""
    checker = False
    
    for x in range(0,len(text)):
        for y in range(0, len(vowels)):
            if text[x] == vowels[y]:
                print(text[x])
                checker = True
                break
        if not checker:
            word += text[x]
        checker = False
    return word
