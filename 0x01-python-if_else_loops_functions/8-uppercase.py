#!/usr/bin/python3
def uppercase(str):
    for c in str:
        str_ord = ord(c)
        if str_ord > 96 and str_ord < 123:
            str_ord -= 32
        print("{}".format(chr(str_ord)), end='')
     print(end='\n')
