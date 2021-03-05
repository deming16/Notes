# General

## Array of Products
```
Write a function that takes in a non-empty array of integers and return an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i]

Sample Input: [5, 1, 4, 2]
Sample Output: [8, 40, 10, 20]

Note that you're expected to solve this problem without division.
```
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

## Shifted Binary Search
```
Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. For example, [1, 2, 3, 4] might have been turned into [3, 4, 1, 2].

The function should use a variation of the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.
```
```python
def shiftedBinarySearch(array, target):
    #
	left = 0
	right = len(array) - 1
	
	while left <= right:
		mid = (right + left) // 2
		if array[mid] == target:
			return mid
		
		# case 1: left half is sorted order, check if target is between left half
		if array[left] < array[mid]:
			if target < array[mid] and target >= array[left]:
				right = mid - 1
			else:
				left = mid + 1
		else:
		# case 2: left half is not in sorted order, right is in sorted order
			if target > array[mid] and target <= array[right]:
				left = mid + 1
			else:
				right = mid - 1
	
	return -1
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

## 4 Sums
```
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all the quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.

if no four numbers sum up to the target sum, the function should return an empty array.
```
```python
def fourNumberSum(array, targetSum):
	allPairSums = {}
	quadruplets = []
	# Start from 1 since first pass won't find anything
	for i in range(1, len(array) - 1):
		
		# For numbers after index i, check if targetSum minus the sum of i and j
		# is in the pair sums, if it is add to quadruplets
		for j in range(i + 1, len(array)):
			currentSum = array[i] + array[j]
			diff = targetSum - currentSum
			if diff in allPairSums:
				for pair in allPairSums[diff]:
					quadruplets.append(pair + [array[i], array[j]])
		
		# For numbers before index i, add them to the pair sums 
		for k in range(0, i):
			currentSum = array[k] + array[i]
			if currentSum not in allPairSums:
				allPairSums[currentSum] = [[array[k], array[i]]]
			else:
				allPairSums[currentSum].append([array[k], array[i]])
	
	return quadruplets
```

## Subarray Sort
```
Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order).

If the input array is already sorted, the function should return [-1, -1]

Input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: [3, 9]
```
```python
def subarraySort(array):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range(len(array)):
		# iterate the array and find out of order
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(num, minOutOfOrder)
			maxOutOfOrder = max(num, maxOutOfOrder)
		
	# Check if its already sorted
	if minOutOfOrder == float("inf"):
		return [-1, -1]
	# if not sorted, find the left index using min out of order number
	leftIdx = 0
	while minOutOfOrder >= array[leftIdx]:
		leftIdx += 1
	rightIdx = len(array) - 1
	# then find the right index using max out of order number
	while maxOutOfOrder <= array[rightIdx]:
		rightIdx -= 1
	
	return [leftIdx, rightIdx]
    pass


def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i + 1]
	if i == len(array) - 1:
		return num < array[i - 1]
	return num > array[i + 1] or num < array[i - 1]
```

## LargestRange
```
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of integers contained in that array.

The first number in the output array should be the first number in the range, while the second number should be the last number in the range.

A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.

you can assume that there will only be one largest range.
```
```python
def largestRange(array):
	# setup hashmap for visited numbers, longest length and longest range
	nums = {}
	longestLength = 0
	longestRange = []
	for num in array:
		nums[num] = False
	# Iterate through the array:
	for num in array:
		if nums[num]:
			continue
		# a. For each number, traverse left and right to find range
		# b. mark number as visited and increment current length
		currLength = 1
		nums[num] = True
		left = num - 1
		right = num + 1
		while left in nums and not nums[left]:
			currLength += 1
			left -=1
		while right in nums and not nums[right]:
			currLength += 1
			right += 1
		# d. Update longest length so far and range
		if currLength > longestLength:
			longestLength = currLength
			longestRange = [left + 1, right - 1]
			
		# c. stop when we reached a visited number on both sides
	return longestRange
```

## Min Rewards
``` Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules:
	1) All students must receive at least one reward
	2) Any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score an must receive strictly fewer rewards than an adjacent student with a higher score.

Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students to satisfy the two rules.

You can assume that all students have different scores; in other words, the scores are all unique.
```
```python
def minRewards(scores):
    # Using Peaks and Valleys method
	# Keep track of: the rewards ar# case 2: left half is not in sorted orderray
	length = len(scores)
	rewards = [1 for _ in range(length)]
	currIdx = 0
	boundaryIdx = -1
	# Iterate through the array
	while currIdx < length:
		# a. When i find a valley, Traverse left and right until local peak
		if ((currIdx == length - 1 or scores[currIdx] < scores[currIdx + 1])
			and (currIdx == 0 or scores[currIdx] < scores[currIdx - 1])):
			left = currIdx - 1
			right = currIdx + 1
			while left >= 0 and scores[left] > scores[left + 1]:
				rewards[left] = max(rewards[left + 1] + 1, rewards[left])
				left -= 1
			while right < length and scores[right] > scores[right - 1]:
				rewards[right] += rewards[right - 1]
				right += 1
			currIdx = right
			boundaryIdx = right - 1
			continue
		# b. continue from the peak on the right
		currIdx += 1
	print(rewards)
	return sum(rewards)
```