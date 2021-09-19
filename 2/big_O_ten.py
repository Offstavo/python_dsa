# How to measure recursive algorithm that make multiple call
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)