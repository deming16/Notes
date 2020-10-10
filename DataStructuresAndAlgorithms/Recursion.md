## Nth Fibonacci
```
Nth Fibonacci, f(n) = (n - 1)th + (n - 2)th
when f(1) = 0, f(2) = 1
find f(n)
```
```python
def getNthFib(n):
    # Write your code here.
	if n == 1:
		return 0
	if n == 2:
		return 1
	lastTwo = [0,1]
	for _ in range(3, n+1):
		temp = lastTwo[0]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = lastTwo[1] + temp
	
	return lastTwo[1]
    pass
```
## Permutations
```
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Case: when there is only one number left
        # The number itself will then be the only permutation
        if len(nums) <= 1:
            return [nums]
        answer = []
        for i, num in enumerate(nums):
            # Create array with all values except num
            n = nums[:i] + nums[i+1: ]
            # For each permutation y...
            for y in self.permute(n):
                # Permutation will be the permutations of rest of the
                # numbers plus the current number
                answer.append([num] + y)
                
        return answer
```