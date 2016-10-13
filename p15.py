
def pascals_triangle(n):
    x=[[1]]
    for i in range(n-1):
        x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
    return x

def solve():
    # It turns out that the number of paths follow the pattern as
    # The middle number of pascal triangle in the odd numbered rows
    # For a 20x20 grid
    rows = 20
    columns = 20
    triangle = pascals_triangle(2*rows + 1)
    return triangle[2*rows][columns]
    
print "Answer by traditional method:", solve()
