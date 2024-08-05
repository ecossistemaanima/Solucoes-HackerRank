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

# Alternativa:
def mini_max_sum(arr):
    length = len(arr) - 1
    max_val = arr[0]
    min_val = arr[0]
    total_sum = 0

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    for num in arr:
        total_sum += num

    print(total_sum - max_val, total_sum - min_val)

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    mini_max_sum(arr)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)
