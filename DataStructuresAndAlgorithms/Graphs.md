# Graphs

## Terms and Definition
* Path - Sequence of edges that begin at one vertex and end at another
* Cycle - A path that begins and ends at the **same vertex**

## Types of Graphs
### Directed Graph

### Weighted Directed Graphs

### Undirected Graph

### Complete Graph

## Implementing a graph on code
There are 2 ways of implementing a graph on code:
1. Adjacency matrix
![AdjMatrix](img/AdjacencyMatrix.png)
1. Adjacent list
![AdjList](img/AdjList.png)
### Setting up a graph
#### Creating the node class
#### Connecting the nodes with edges

## Algorithms

### Graph Traversal

#### Breadth First Search (BFS)
##### Iterative Version
```
Q = new Queue;
Q.enqueue(v);
mark v as visited
while(!Q.isEmpty()) {
  curr = Q.dequeue()
  print curr
  for(w : curr.neighbours) {
    if(!w.isVisited {
      Q.enqueue(w);
      w.isVisited = true;
    }
  }
}
```
##### Recursive Version

##### Time Complexity
**O(V+E)**

#### Depth First Search (DFS)
##### Iterative Version
##### Recursive Version

### Sorting