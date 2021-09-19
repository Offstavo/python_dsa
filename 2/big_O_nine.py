# How to measure recursive algorithm
def findMaxNumRec(sampleArray,n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n-1],findMaxNumRec(sampleArray, n-1))