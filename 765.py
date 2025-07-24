from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0

        for i in range(0, n, 2):
            first = row[i]
            partner = first ^ 1  # Partner is either first+1 or first-1
            if row[i+1] != partner:
                partner_index = pos[partner]
                
                # Swap
                row[i+1], row[partner_index] = row[partner_index], row[i+1]
                
                # Update positions
                pos[row[partner_index]] = partner_index
                pos[row[i+1]] = i + 1
                
                swaps += 1

        return swaps
