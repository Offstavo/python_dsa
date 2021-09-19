def factorial(n):  #M(n)
    if n < 0: #O(1)
        return -1
    elif n == 0: #O(1)
        return 1
    else:
        return n * factorial(n-1) #M(n-1)

        # Time complexity O(n)