def isSubsequence(s: str, t: str) -> bool:
    i = 0  # Pointer for s
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)

# Example usage:
print(isSubsequence("abc", "ahbgdc"))  # True
print(isSubsequence("axc", "ahbgdc"))  # False
