class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_dist = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            if abs(gx - target[0]) + abs(gy - target[1]) <= player_dist:
                return False
        return True
