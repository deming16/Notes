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