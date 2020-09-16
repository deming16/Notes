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