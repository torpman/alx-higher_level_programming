#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [True if index % 2 == 0 else False for index in my_list]
    return result
