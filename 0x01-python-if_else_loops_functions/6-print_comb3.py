#!/usr/bin/python3
for j in range(0, 8):
    for k in range(j + 1, 10):
        print("{:d}{:d}".format(j, k), end=', ')
print("{:d}{:d}".format(j + 1, k))
