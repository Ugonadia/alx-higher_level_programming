#!/usr/bin/python3
def islower(c):
    # ord returns the number that represents the unicode code of a character
    c_ord = ord(c)
    if c_ord > 96 and c_ord < 123:
        return True
    else:
        return False
