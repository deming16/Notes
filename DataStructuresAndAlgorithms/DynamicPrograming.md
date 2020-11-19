## Number of Ways To Make Change
```
Given an array of distinct positive integers representing coin denominations and a single non-negative integer n representing at target amount of money, write a function that returns the number of ways to make change for that target amount using the given coin denominations.

Note that an unlimited amount of coins is at your disposal.
```
```python
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	ways = [0 for _ in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for index in range(n+1):
			if denom <= index:
				ways[index] += ways[index-denom]
	
	return ways[n]
    pass
```

## Min Number of Coins for Change
```
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
```
```python
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	minCoins = [float("inf") for _ in range(n+1)]
	minCoins[0] = 0
	
	for denom in denoms:
		for index in range(len(minCoins)):
			if denom <= index:
				minCoins[index] = min(minCoins[index], minCoins[index - denom] + 1)
	
	return minCoins[n] if minCoins[n] != float("inf") else -1
  ```