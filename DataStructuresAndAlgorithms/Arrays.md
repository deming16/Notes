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