class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}
        for index, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    key = (word[:i], word[j:])
                    self.lookup[key] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get((pref, suff), -1)
