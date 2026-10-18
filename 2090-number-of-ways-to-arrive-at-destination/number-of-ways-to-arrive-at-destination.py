import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        adj_lst = [[] for _ in range(n)]
        for u, v, w in roads:
            adj_lst[u].append([v, w])
            adj_lst[v].append([u, w])

        distance = [sys.maxsize for _ in range (n)]
        ways = [0 for _ in range(n)]

        distance[0] = 0
        ways [0] = 1

        priory_queue = [[0, 0]]  # [Dist, Node]
        while len (priory_queue) != 0:
            dist, node = heapq.heappop(priory_queue)
            for adjNode, weight in adj_lst[node]: 
                new_dist = dist + weight
                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priory_queue, [new_dist, adjNode])
                    ways [adjNode] = ways[node]
                elif new_dist == distance[adjNode]:
                    ways[adjNode] += ways[node] % MOD

        return ways[n-1] % MOD
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna