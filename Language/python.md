# Python
## Classes
```python
class ClassName:
    def __init__(self, x):
    self.x = x
```
```python
# Ternery Operation
a = value_when_true if <condition> else value_when_false
# Absolute
a = abs(value)
```
## Numbers
- Max num: `float("inf")`
- Min num: `float("-inf")`
- Absolute: `abs(n)`

## For Loop
```python
for value in array:
  #code
```
```python
for key,value in enumerate(array):
  #code
```
```python
for number in range(n):
  #code
for number in range(lower,upper):
  #upper is not inclusive
  #code
for key,value in dict.items():
```

## While Loop

## Array/List
```python
len(arr) # length of array
[[False for _ in range(col)] for _ in range(row)] # init 0/false for matrix
type(arr) is list # check if list

# ØPERATIONS
append(item) # add to end of list
reversed(arr) # reverse array
arr.pop() # remove last item
arr.remove(val) # remove first item with specified value
```

## Set
- add(item)
- remove(item)
## Dict
```python
map = {}
map.update({key : value})
map.values()
map.keys()
map.pop(key)
```
## Tuple

## String
```python
# a-z --> 97 to 122
# A-Z --> 65 to 90
ord(char) # Return ASCII code of char
chr(code) # Return character given ascii code
string.split(separator, maxsplit)
string.find(value, start, end)
string.isalnum() string.isalpha() string.isnumeric()
string.islower() string.isupper()
string.isspace()
```