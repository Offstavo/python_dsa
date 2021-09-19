# Print fibonacci numbers
def allFib(n):
    for i in range(n):
        print(str(i)+":, "+str(fib(i)))

# Calculate fibonacci numbers
def fib(n): #O(n^2)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

    #Time complexity O(n^2)