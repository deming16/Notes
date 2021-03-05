# Famous Alogrithms

## Euclidean algorithm
This algo is used to find  GCD (Greatest Common Divisor) or HCF (Highest Common Factor). Aka, the largest number that divides both of them.

```python
def gcd(a,b):
     
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)
```