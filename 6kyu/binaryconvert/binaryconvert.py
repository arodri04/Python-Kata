#!/usr/bin/env python3

def binaryconvert(num):
    binnum = bin(num).lstrip('-0b')
    count = 0
    for i in binnum:
        if int(i) == 1:
            count += 1
    return count

