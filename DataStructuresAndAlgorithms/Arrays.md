# General

## Array of Products
```
Write a function that takes in a non-empty array of integers and return an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i]

Sample Input: [5, 1, 4, 2]
Sample Output: [8, 40, 10, 20]

Note that you're expected to solve this problem without division.

## Longest Peak
```
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers [1, 4, 10, 2] form a peak, but the integers [4, 0, 10] don't and neither do the integers [1, 2, 2, 0]. Similarly, the integers [1, 2, 3] don't form a peak because there aren't any strictly decreasing integers after the 3.
```
```python
def longestPeak(array):
    # 1. Traverse the array
	# 2. When a peak is found, traverse left and right from peak to calculate length of peak
	# 3. Update the longest peak accordingly
	longestPeak = 0
	for i in range(1, len(array) - 1):
		if array[i] > array[i-1] and array[i] > array[i+1]:
			currPeak = 3
			j = i - 2
			while j >= 0 and array[j] < array[j+1]:
				currPeak += 1
				j -= 1
				
			j = i + 2
	
			while j < len(array) and array[j] < array[j-1]:
				currPeak += 1
				j +=1
			
			longestPeak = currPeak if currPeak > longestPeak else longestPeak
	
	return longestPeak
    pass
```

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

## Maximum Sum Subarray (Kadane's Algorithm)
```
write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all of the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers.           

Sample Input = [3, 4, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
Sample Output: 19
```
```python
def kadanesAlgorithm(array):
	maxSum = float("-inf")
	currSum = 0
	
	for num in array:
		currSum += num
		if currSum > maxSum:
			maxSum = currSum
		if currSum < 0:
			currSum = 0
	
	return maxSum
```