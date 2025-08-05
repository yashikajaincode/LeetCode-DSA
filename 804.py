class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        
        for word in words:
            code = ''.join(morse[ord(c) - ord('a')] for c in word)
            transformations.add(code)
        
        return len(transformations)
