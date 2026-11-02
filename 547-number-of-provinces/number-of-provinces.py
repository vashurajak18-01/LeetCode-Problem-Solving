
from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node) :
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return 

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        ds = DisjointSet(V)

        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    ds.union(i, j)

        count = 0
        for i in range(V):
            if ds.find(i) == i:
                count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna