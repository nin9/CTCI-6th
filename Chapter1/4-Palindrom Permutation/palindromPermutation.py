from collections import defaultdict
def charNum(c) -> int:
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    c = ord(c)
    
    if a <= c <= z:
        return c - a
    elif A <= c <= Z:
        return c - A
    else:
        return -1

"""
Time Complexity O(n)
Space Complexity O(n)
"""
def palindromPermutation(s: str) -> bool:
    m = defaultdict(int)
    oddCount = 0
    for c in s:
        c = charNum(c)
        if c == -1:
            continue
        m[c]+=1
        if m[c]%2:
            oddCount+=1
        else:
            oddCount-=1
    return oddCount <= 1
