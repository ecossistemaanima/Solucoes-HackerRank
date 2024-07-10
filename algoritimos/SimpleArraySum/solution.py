def simpleArraySum(ar):
    # Jeito simples | usando built-in methods.
    # return sum(ar)

    # Jeito tradicional - O(N)
    sum_counter = 0

    for n in ar:
        sum_counter += n

    return sum_counter

if __name__ == '__main__':
    array = [1, 2, 3]
    print(simpleArraySum(array))
