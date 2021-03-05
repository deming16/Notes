## Climbing Stairs
Can take 1 or 2 steps. How many ways i can get to the top?
```python
# f(n) = f(n-1) + f(n-2)
def climbStairs(n):
  dp = [0 for _ in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]
```

## Coin Change
Get an amount with least number of coins
coin vals: {1, 2, 5}
n = 6 cents
1 + 1 + 1 + 1 + 1 + 1 = 6 cents (6 coins)
1 + 5 = 6 cents (5 coins)
```python
# coins = set({1, 2, 5})
def coinChange(coins,amount):
  dp = [float("inf") for _ in range(amount+1)]
  dp[0] = 0 # base case

  for i in range(len(dp)):
    for coin in coins:
      if i - coin >=0:
        dp[i] = min(dp[i], dp[i-coin]+1)
      

  return dp[amount]
```

## Longest Increasing Subsequence
[2,4,1,6,3,9] --> 2, 4, 6, 9 length 4
```python
def LIS(arr):
  dp [0 for _ in range(len(arr))]
  dp[0] = 1

  maxLength = 1;
  for i in range(len(dp)):
    currMax = 0
    for j in range(i):
      if arr[i] > arr[j]:
        currMax = max(currMax, dp[j])
    
    dp[i] = currMax + 1
    maxLength = max(dp[i], maxLength)

  
  return maxLength
```

## Word Break
Check if a string can be broken into valid words
validWords : {"dog", "g", "food", "do"}
s = "dogfood" --> T broken into "dog" and "food"
```python
def wordBreak(s, dict):
  dp = [False for _ in range(len(s) + 1)]
  dp[0] = True

  for i in range(1, len(dp)):
    for j in range(i):
      # Check if substring before j can be split into valid words
      # and if substring between j and i is valid
      if dp[j] and dp[j:i+1] in dict:
        dp[i] = True
        break

  
  return dp[len(s)]
```
