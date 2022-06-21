#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer and handles exceptions"""
    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
