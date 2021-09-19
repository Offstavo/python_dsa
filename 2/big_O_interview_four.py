def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)): #O()
        for j in range(len(arrayB)): #O()
            if arrayA[i] < arrayB[i]: #O(1)
                print(str(arrayA[i]) + "," +str(arrayB[j])) #O(1)

# b = len(arrayB)
# a = len(arrayA)
#Time complexity O(a,b)