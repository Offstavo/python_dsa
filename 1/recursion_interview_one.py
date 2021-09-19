# How to find the sum of digits of a positive integer number using recursion

def sumOfDigits(n):
    assert n>=0 and int(n) == n, 'The number has to be a positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n/10))

sumOfDigits(4)