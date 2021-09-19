def printUnorderedPairs(array):
    for i in range(0,len(array)): #O(n)
        for j in range(i+1,len(array)): #O(n^2)
            print(array[i]+","+array[j]) #O(1)

# Time complexity O(n^2)