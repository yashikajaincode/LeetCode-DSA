class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diff = 0
            for c1, c2 in zip(word, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False

# Example usage (for VS or local testing)
if __name__ == "__main__":
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello", "leetcode"])
    print(magicDictionary.search("hello"))     # False
    print(magicDictionary.search("hhllo"))     # True
    print(magicDictionary.search("hell"))      # False
    print(magicDictionary.search("leetcoded")) # False
