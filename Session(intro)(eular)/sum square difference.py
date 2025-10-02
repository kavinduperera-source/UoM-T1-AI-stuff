n=100
normal_sum = int((n*(n+1))/2)
normal_sum_square = normal_sum*normal_sum
sq_sum = int((n*(n+1)*(2*n+1))/6)
sum_sq_diff = int(normal_sum_square-sq_sum)
print(sum_sq_diff)