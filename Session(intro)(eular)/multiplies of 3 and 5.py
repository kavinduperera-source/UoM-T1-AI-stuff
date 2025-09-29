def sum_multiplies(limit):
    the_sum = 0
    for num in range(limit):
        if num % 3 == 0 or num  % 5 == 0:
            the_sum = the_sum + num
    return the_sum

limit = 1000
print(sum_multiplies(limit))
        