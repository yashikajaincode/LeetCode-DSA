class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # Check missing types
        missing_lower = int(not any(c.islower() for c in password))
        missing_upper = int(not any(c.isupper() for c in password))
        missing_digit = int(not any(c.isdigit() for c in password))
        missing_types = missing_lower + missing_upper + missing_digit

        # Count repeating sequences
        repeats = []
        i = 2
        count = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        # Case 1: Too short
        if n < 6:
            return max(missing_types, 6 - n)

        # Case 2: Length OK (6 to 20)
        if n <= 20:
            replacements = 0
            for length in repeats:
                replacements += length // 3
            return max(missing_types, replacements)

        # Case 3: Too long (> 20)
        over_len = n - 20
        replacements = 0
        buckets = [0, 0, 0]  # repeats with mod 3 == 0, 1, 2

        for length in repeats:
            replacements += length // 3
            buckets[length % 3] += 1

        # Use deletions to reduce replacements
        # First target mod 0 sequences (need 1 deletion to reduce one replacement)
        to_delete = over_len
        for i in range(3):
            while buckets[i] > 0 and to_delete > i:
                to_delete -= (i + 1)
                buckets[i] -= 1
                replacements -= 1

        replacements = max(0, replacements - to_delete // 3)

        return over_len + max(missing_types, replacements)
