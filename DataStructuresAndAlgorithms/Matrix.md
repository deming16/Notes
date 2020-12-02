# Overview
Matrix Problems can be classified into these types:
1. DFS/BFS
1. Searching for values by elimination
1. Simulation of matrix traversal
1. Backtracking

## Search in Sorted Matrix
```
You're given a matrix of distinct integers and a target integer. Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1].
```
```python
def searchInSortedMatrix(matrix, target):
	row, col = 0, len(matrix[0]) - 1
	
	while row <= len(matrix[0]) - 1 and col >= 0:
		if matrix[row][col] == target:
			return [row,col]
        # If number is too big, means anything below is also too big so we don't want the entire column
		elif matrix[row][col] > target:
			col -= 1
        # If the number is too small, means anything to the left is also too small so we don't want the entire row
		else:
			row += 1
	
	return [-1,-1]
```

# Simulation
## Spiral Matrix
```
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge case: Empty matrix
        if not matrix: return []
        
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        # setup direction - right, down, left and up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        # di is 0 initially because starting with left
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            # traverse
            cr, cc = r + dr[di], c + dc[di]
            # Once reached boundary, change direction (di)
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        return ans
```