# How to convert a number from decimal to binary using recursion
def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    if n == 0:
        return 1
    else:
        return n%2 + 10 * decimalToBinary(int(n/2))

print(decimalToBinary(10))