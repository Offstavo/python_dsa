def printUnorderedPairs(arrayA,arrayB):
    for i in range(len(arrayA)): #O()
        for j in range(len(arrayB)): #O()
            for k in range(0,100000): #O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) #O(1)

# Time complexity O(a,b)