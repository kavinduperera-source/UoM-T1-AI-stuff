def is_palindrome_product(num1,num2):
    product = str(num1*num2)
    return product == product[::-1]

digits = 3
num1 = int("9"*digits)
num2 = int("9"*digits)


def largest_product(num1,num2):
    largest = 0
    original_num2 = num2
    while num1 > 0:
        num2 = original_num2
        while num2 > 0:
            product = num1*num2
            if is_palindrome_product(num1,num2) and largest<product:
                largest = product
            num2 -= 1
        num1 -= 1
    return largest

print(largest_product(num1,num2))