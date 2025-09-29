def even_fib(limit):
    a , b = 1 , 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total = total + a
        a , b = b , a+b
    return total

print(even_fib(4000000))