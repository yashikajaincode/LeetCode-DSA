def intToRoman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    roman = []
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            roman.append(syms[i])
    
    return ''.join(roman)

# Example usage
if __name__ == "__main__":
    print(intToRoman(3749))   # Output: "MMMDCCXLIX"
    print(intToRoman(58))     # Output: "LVIII"
    print(intToRoman(1994))   # Output: "MCMXCIV"
