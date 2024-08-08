def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_counter = 0
    for apple in apples:
        if s <= a + apple <= t:
            apples_counter += 1

    orange_counter = 0
    for orange in oranges:
        if s <= b + orange <= t:
            orange_counter += 1

    print(apples_counter)
    print(orange_counter)