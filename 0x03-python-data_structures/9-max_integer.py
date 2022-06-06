#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = my_list[0]
    for element in my_list:
        if mx < element:
            mx = element
    return mx
