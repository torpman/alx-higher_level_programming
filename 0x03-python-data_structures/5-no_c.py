#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            newString += ch
    return newString
