#!/bin/python3

def plusMinus(arr):
    n = len(arr)
    positive_v = len(list(filter(lambda x: x > 0, arr)))
    negative_v = len(list(filter(lambda x: x < 0, arr)))
    zeros = len(list(filter(lambda x: x == 0, arr)))

    print(f"{positive_v / n:.6f}")
    print(f"{negative_v / n:.6f}")
    print(f"{zeros / n:.6f}")

if __name__ == '__main__':
    """Code Below is only for tests"""
    arr = [1, 1, 0, -1, -1]
    result = plusMinus(arr)