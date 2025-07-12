def isPalindrome(s: str) -> bool:
    # Filter alphanumeric and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    return filtered == filtered[::-1]

# Example usage:
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                      # False
print(isPalindrome(" "))                               # True
