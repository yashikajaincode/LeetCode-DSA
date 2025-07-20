from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        new_line = []
        result = []

        for line in source:
            i = 0
            if not in_block:
                new_line = []

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False
                    i += 2
                elif not in_block:
                    new_line.append(line[i])
                    i += 1
                else:
                    i += 1

            if not in_block and new_line:
                result.append(''.join(new_line))

        return result
