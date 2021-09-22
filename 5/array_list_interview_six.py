# Permutation 

def permutation(list1, list2):
    print(list1)
    list2.reverse()
    if list1 == list2:
        return True
    else:
        return False

print(permutation([1,2,3],[3,2,1]))