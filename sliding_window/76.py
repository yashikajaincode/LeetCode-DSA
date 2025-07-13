from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    t_count = Counter(t)
    window_count = {}
    have, need = 0, len(t_count)
    res = [float('inf'), 0, 0]
    left = 0

    for right, char in enumerate(s):
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        while have == need:
            if (right - left + 1) < res[0]:
                res = [right - left + 1, left, right]
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res[1], res[2]
    return s[l:r+1] if res[0] != float('inf') else ""

# Example usage
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(minWindow("a", "a"))                # Output: "a"
print(minWindow("a", "aa"))               # Output: ""
