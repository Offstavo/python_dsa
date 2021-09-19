#recursion using factorial

# Step 1 recursive case - the flow
# Step 2 base condition - the stopping criterion
# Step 3 Unintentional case - the constraint
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be postive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))