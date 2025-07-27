from collections import defaultdict, deque
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        # Min heap: (total_cost, current_city, stops_used)
        heap = [(0, src, 0)]
        # visited[city] = minimum stops used to reach that city
        visited = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            # If we have visited city with fewer stops before, skip
            if city in visited and visited[city] <= stops:
                continue
            visited[city] = stops

            if stops <= k:
                for nei, price in graph[city]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1
