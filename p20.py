cache = {}

def factorial(n):
    """
    Memoized recursive function for the above expression
    """
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = 1
        return cache[1]
    else:
        cache[n] = n * factorial(n - 1)
        return cache[n]

def the_simple_method():
    number = 100
    ans = reduce(lambda x,y: int(x) + int(y), str(factorial(number)))
    return ans


print "Answer by simple chain method:", the_simple_method()
