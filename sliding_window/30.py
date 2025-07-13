from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = Counter(words)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(0, total_len, word_len):
            word = s[i + j:i + j + word_len]
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                break
        else:
            result.append(i)

    return result

# Example usage
print(findSubstring("barfoothefoobarman", ["foo","bar"]))  # Output: [0,9]
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # Output: []
print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # Output: [6,9,12]
