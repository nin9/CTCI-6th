def checkEdit(s1: str, s2: str) -> bool:
    i = j = 0
    foundDiff = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if foundDiff:
                return False
            foundDiff = True
        i+=1
        j+=1
    return True
    

def checkInsert(s1: str, s2: str) -> bool:
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            i+=1
        else:
            i+=1
            j+=1
    return True

"""
Time Complexity O(n), where n is length of s1 or s2 it doesn't matter which one of them
 because at most they will differ by 1 ( the function would return false right away otherwise)
Space Complexity O(1)
"""
def oneAway(s1: str, s2: str) -> bool:
    l1, l2 = len(s1), len(s2)
    if abs(l1 - l2) > 1: return False
    
    if l1 == l2:
        return checkEdit(s1, s2)
    elif l1 > l2:
        return checkInsert(s1, s2)
    else:
        return checkInsert(s2, s1)
