#!/bin/python3

def staircase(n):
    for level in range(1, n + 1):
        spaces = n - level
        hashes = level
        print(" " * spaces + "#" * hashes)

if __name__ == '__main__':
    n = 6
    staircase(n)