#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv) - 1
    if total == 0:
        print("{:d} arguments.".format(total))
        exit()

    if total == 1:
        print("{:d} argument:".format(total))
        for x in sys.argv[1:]:
	    print("{}: {}".format(total, x))
    if total > 1:
        print("{} arguments:".format(total))
        for x, n in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(x, n))
