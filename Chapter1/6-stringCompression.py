"""
Time Complexity O(n)
Space Complexity O(n)
"""
def stringCompression(s: str) -> str:
    if not s: return ""
    compressedS = []
    
    i = 0
    while i < len(s):
        j = i+1
        count = 1
        while j < len(s) and s[j] == s[i]:
            count+=1
            j+=1
        compressedS.append(s[i])
        compressedS.append(str(count))
        i = j
    return "".join(compressedS) if len(compressedS) < len(s) else s
