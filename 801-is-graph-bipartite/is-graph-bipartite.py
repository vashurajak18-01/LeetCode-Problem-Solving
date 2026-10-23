class Solution:
    def dfs(self, current_node, visited, graph, colour):
        visited[current_node] = colour
        for adjNode in graph[current_node]:
            if visited[adjNode] != -1:
                # 0, 1
                if visited[adjNode] == colour:
                    return False
            else:
                if colour == 0:
                    ans = self.dfs(adjNode, visited, graph, 1)
                else:
                    ans = self.dfs(adjNode, visited, graph, 0)
                if ans == False:                 
                    return False
        return True



    def isBipartite(self, graph: list[list[int]]) -> bool:
        total_nodes = len(graph)
        visited = [-1] * total_nodes
        for  index in range(0, total_nodes):
            if visited[index] == -1:
                ans = self.dfs(index, visited, graph, 0)
                if ans == False:
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna