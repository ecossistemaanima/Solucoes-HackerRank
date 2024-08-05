def birthdayCakeCandles(candles):
    max_height = max(candles)
    count_max_height = candles.count(max_height)
    return count_max_height

if __name__ == '__main__':
    arr = [4, 3, 4, 1]
    print(birthdayCakeCandles(arr))

