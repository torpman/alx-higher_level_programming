#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listLen = len(my_list)
    for i in range(listLen):
        print("{:d}".format(my_list[listLen - 1]))
        listLen -= 1
