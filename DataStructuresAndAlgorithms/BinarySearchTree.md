## Find Closest Value in BST
```
Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest.
Each BST node has an integer value, a left child node, and a right child node/ A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None/null.
```
```python
def findClosestValueInBst(tree, target):
    # Write your code here.
	currNode = tree
	smallestDiff = float("inf")
	closest = None
	while currNode != None:
			if target == currNode.value:
				return target
			if abs(currNode.value - target) < smallestDiff:
				smallestDiff = abs(currNode.value - target)
				closest = currNode.value
			if target < currNode.value:
				currNode = currNode.left
			elif target > currNode.value:
				currNode = currNode.right
	
	return closest
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```
## Find Lowest Common Ancestor
```
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root
        
        while curr != None:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
```