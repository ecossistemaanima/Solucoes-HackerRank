#!/bin/python3

def miniMaxSum(arr):
    curr_sum_min = float('inf')
    curr_sum_max = float('-inf')
    total_sum = sum(arr)

    for i in range(len(arr)):
        curr_value = total_sum - arr[i]
        curr_sum_max = max(curr_sum_max, curr_value)
        curr_sum_min = min(curr_sum_min, curr_value)

    print(f"{curr_sum_min} {curr_sum_max}")

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
