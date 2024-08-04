def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = low + (high - low) // 2
        middle_val = nums[middle]

        if middle_val == target:
            return True
        elif middle_val < target:
            low = middle + 1
        else:
            high = middle - 1

    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    found = binary_search(arr, target)
    if found:
        print(f"The target {target} was found in the array.")
    else:
        print(f"The target {target} was not found in the array.")
