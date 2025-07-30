from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            waiting[word[0]].append((word, 1))
        
        count = 0
        for c in s:
            for _ in range(len(waiting[c])):
                word, i = waiting[c].popleft()
                if i == len(word):
                    count += 1
                else:
                    waiting[word[i]].append((word, i + 1))
        return count
