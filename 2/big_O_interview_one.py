# Runtime of the code
def foo(array):
    sum = 0 #O(1)
    product = 1 #O(1)

    for i in array: #O(n)
        sum += i #O(1)
    
    for i in array: #O(n)
        product *= i #O(1)
    print("Sum ="+str(sum)+", Product ="+str(product)) #O(1)

# Timecomplexity = O(n)