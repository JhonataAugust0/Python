#!/usr/bin/env python3

def e(a, b):
    if a and b:
        return True
    else:
        return False

def ou(a, b):
    if (not a) and (not b):
        return False
    else:
        return True


A = [True, True, False, False]
B = [True, False, True, False]

for a, b in zip(A, B):
    print("{} V {} = {}".format(a, b, ou(a, b)))
