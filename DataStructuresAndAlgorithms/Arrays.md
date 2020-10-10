# Hashing
## 2Sum
```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```python
def twoNumberSum(array, targetSum):
    # Write your code here.
	numHash = {}
	
	for i,v in enumerate(array):
		if targetSum - v in numHash:
			return [numHash[targetSum - v], i]
		else:
			numHash.update({v: i})
	return []
    pass

```

# Pointers
## Validate Subsequence
```
Given two non-empty arrays of integers, write a function that determines whether the second array 
is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] and so do that numbers [2,4]. Note that a single number in an array and the array itself are both valid subsequences of the array
```
```python
def isValidSubsequence(array, sequence):
    # Write your code here.
	aIndex = 0
	bIndex = 0
	for v in array:
		if sequence[bIndex] == v:
			bIndex += 1
		if bIndex == len(sequence):
			return True
	
	return False
    pass
```
# Binary Search
## Binary Search on Sorted List
```
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (right + left) // 2
            # Return if number match
            if nums[mid] == target:
                return mid
            # Need to search on right half
            if nums[mid] < target:
                left = mid + 1
            # Need to search on left half otherwise
            else:
                right = mid - 1
        
        return -1
```

## Find Smallest Letter Greater than Target
```
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'
```
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left < right:
            mid = (right + left) // 2
            # Need something larger so have to search right half 
            print(letters[mid])
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return letters[0] if letters[left] <= target else letters[left]
```

## Peak Index in a Mountain Array
```
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
```
```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (right + left) // 2
                              
            # Not strictly means mountain is still within this range so continue on left half
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
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