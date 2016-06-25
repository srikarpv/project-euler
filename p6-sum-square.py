def traditional():
    n = 100
    square_of_sum = (n**2) * (n+1)**2 / 4
    sum_of_square = n * (n+1) * (2*n+1) / 6
    diff = square_of_sum - sum_of_square
    return diff

print "Answer by traditional method:",traditional()
