# Recursion using fibonacci 

# Step 1 recursive case - the flow
# Step 2 base condition - the stopping criterion
# Step 3 Unintentional case - the constraint

def fibonacci(n):
    assert n >= 0 and int(n) == n , 'Fibonacci number cannot be in negative number of non integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))