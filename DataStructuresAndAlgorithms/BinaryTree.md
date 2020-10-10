# 1. Tree Traversal
## Binary Tree Level Order Traversal in Reverse
```
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        queue = list()
        queue.append([root, 0])
        level = -1
        while len(queue) > 0:
            node = queue.pop(0)
            if node[0].left != None:
                queue.append([node[0].left, node[1] + 1])
            if node[0].right != None:
                queue.append([node[0].right, node[1] + 1])
            if level != node[1]:
                res.append([node[0].val])
                level = node[1]
            else:
                res[level].append(node[0].val)
                
        return reversed(res)
```