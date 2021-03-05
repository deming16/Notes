## Number of Connected Components in an Undirected Graph
```python
def countComponents(n, edges):
  adj = {}
  for i in range(n):
    adj[i] = []

  for i in range(len(edges)):
    adj[edges[i][0]].append(edges[i][1])
    adj[edges[i][1]].append(edges[i][0])

  visited = [False for _ in range(n)]
  count = 0

  for i in range(n):
    if not visited[n]:
      count += 1
      dfs(adj, i, visited)
  
  return count

def dfs(adj, i, visited):
  visited[i] = True

  for j in range(len(adj[i])):
    if not visited[adj[i][j]]:
      dfs(adj, adj[i][j], visited)
```

## Course Schedule
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
            
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        
        def hasCycle(adj, i, visited):
            if visited[i] == -1:
                return True
            if visited[i] == 1:
                return False
            visited[i] = -1

            for j in range(len(adj[i])):
                if hasCycle(adj, adj[i][j], visited):
                    return True
        
            visited[i] = 1
            return False
        
        visited = [0 for _ in range(numCourses)]
        
        for i in range(numCourses):
            if visited[i] == 0:
                if hasCycle(adj, i, visited):
                    return False
        
        return True
```

## Possible Bipartition
```python
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = {}
        for i in range(N+1):
            adj[i] = []
        
        for i in range(len(dislikes)):
            adj[dislikes[i][0]].append(dislikes[i][1])
            adj[dislikes[i][1]].append(dislikes[i][0])
            
        
        visited = [0 for _ in range(N+1)]
    
        for i in range(1,N+1):
            if visited[i] == 0:
                if not self.dfs(adj, i ,visited, 1):
                    return False
        
        return True
    
    def dfs(self, adj, i, visited, group):
        
        visited[i] = group

        for j in adj[i]:
            if visited[j] == group:
                return False
            if visited[j] == 0 and not self.dfs(adj, j, visited, group * -1):
                return False

        return True
```

## Min Height Trees
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        leaves = []
        for key,value in graph.items():
            if len(value) == 1:
                leaves.append(key)
                
        num = n
        while num > 2:
            newLeaves = []
            for leaf in leaves:
                node = graph[leaf][0]
                graph[node].remove(leaf)
                graph[leaf].remove(node)
                if len(graph[node]) == 1:
                    newLeaves.append(node)
            
            num -= len(leaves)
            leaves = newLeaves
            
        return leaves if len(leaves) != 0 else [0]
```