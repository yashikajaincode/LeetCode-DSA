from collections import defaultdict
from typing import Tuple

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(i: int) -> Tuple[defaultdict, int]:
            count = defaultdict(int)
            while i < len(formula):
                if formula[i] == '(':
                    sub_count, i = parse(i + 1)
                    start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[start:i] or '1')
                    for atom, c in sub_count.items():
                        count[atom] += c * multiplier
                elif formula[i] == ')':
                    return count, i + 1
                else:
                    start = i
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        i += 1
                    atom = formula[start:i]
                    start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    cnt = int(formula[start:i] or '1')
                    count[atom] += cnt
            return count, i

        atom_count, _ = parse(0)
        return ''.join(atom + (str(atom_count[atom]) if atom_count[atom] > 1 else '') for atom in sorted(atom_count))
