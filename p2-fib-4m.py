def fibonacci():
    """
    Just the usual fibonacci generator which starts from 1,2,3,..
    """
    a = 1
    b = 2
        
    while True:
        yield a
        sum_ = a + b
        a = b
        b = sum_
        
def mod_fibonacci():
    """
    A modified version which returns every third number from 1,1,2,3,5,8,..
    Note: Every third number is an even number
    """
    a = 1
    b = 1
    c = a + b
    while True:
        yield c
        a = b + c
        b = c + a
        c = a + b
        
def default():
    """
    Function to calculate sum of the usual fibonacci
    """
    sum_ = 0
    for x in fibonacci():
        if x >= 4000000:
            break
        if x % 2 == 0:
            sum_ = sum_ + x
    return sum_
    
def third_number():
    """
    Function to calculate the sum out of the modified fibonacci
    """
    sum_ = 0
    for x in mod_fibonacci():
        print x
        if x >= 4000000:
            break
        sum_ = sum_ + x
    return sum_

print "Answer by default method:",default()
print "Answer by optimized method:",third_number()
