## Word Search
```
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        
        def word_search(r, c, index, word):
            if index == len(word):
                return True
            
            if (r < 0 or r >= len(board) or 
                c < 0 or c >= len(board[0]) or 
                board[r][c] != word[index] or
                visited[r][c] == True):
                return False
                
            visited[r][c] = True;
            
            if (word_search(r + 1, c, index + 1, word) or
                word_search(r - 1, c, index + 1, word) or
                word_search(r, c + 1, index + 1, word) or
                word_search(r, c - 1, index + 1, word)):
                
                return True
            
            #BackTrack if not found
            visited[r][c] = False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and word_search(i, j, 0, word):
                    return True
        
        return False
```

## Combination Sum
```
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
```
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(curr = [], currSum = 0, startIndex = 0):
            if currSum == target:
                answer.append(curr[:])
                return
            if currSum > target:
                return
                
            for i in range(startIndex, n):
                curr.append(candidates[i])
                backtrack(curr, currSum + candidates[i], i)
                curr.pop()

        n = len(candidates)
        backtrack()
        
        return answer
```