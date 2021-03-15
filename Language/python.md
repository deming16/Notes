# Python/JavaScript for Coding Interviews

## Classes
```javascript
class ClassName {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
}
```
```python
class ClassName:
    def __init__(self, x):
    self.x = x
```

## Ternery Operation
```javascript
a = condition ? valueWhenTrue : valueWhenFalse
```
```python
# Ternery Operation
a = value_when_true if <condition> else value_when_false
```
## Numbers
```javascript
absolute = Math.abs(num) // Absolute number
maxNum = Infinity // Maximum number
minNum = -Infinity // Minimum number
Math.floor(y/x) // Integer Division
```
```python
absolute = abs(value) # Absolute number
maxNum = float("inf") # Maximum number
minNum = float("-inf") # Minimum number
x // y # Integer Division
```

## For Loops
```javascript
for (let i = 0; i < limit; i++){}
for (let value of array) {}
for (let key of Object.keys(obj)) {}
for (var i of map.keys()) {}
```
```python
for value in array:
for key,value in enumerate(array):
for index in range(n):
for number in range(lower,upper):
```

## Type Checking
```javascript
Number.isInteger(num) // Check int
typeof str === "string" // Check string
Array.isArray(arr) // Check array
```
```python
isinstance(num, int) # Check int
isinstance(string, str) # Check string
type(arr) is list # Check if list
```

## Casting
```javascript
parseInt(str) // Convert to int
num.toString(base) // Convert to string
```
```python
int(string) # Convert to int
str(num) # Convert to string
```

## Array/List
```javascript
arr.length // Length of array
Array(R).fill().map(() => Array(C).fill(false)) // Init 0/false for matrix
Array(R).fill(0) // init 0/false for array

// Sorting
arr.sort() // Sort in desc
arr.sort((a, b) => a - b) // Sort in asc
arr.reverse() // reverse array
// Adding
arr.push() // add element to end of array
arr.concat(arr1) // concat 2 arrays
// Deleting
arr.pop() // pop element from end of array
arr.shift() // remove first element
arr.splice(arr.indexOf(x), 1) // Delete element at index x
// Making Copies
arr.slice(x, y) // return array from index [x, y), array.slice() to make a copy
```
```python
len(arr) # length of array
[[False for _ in range(col)] for _ in range(row)] # init 0/false for matrix

# Sorting
reversed(arr) # reverse array
# Adding
append(item) # add to end of list
list1 + list2 # concat two list
# Deleting
arr.pop() # remove last item
arr.remove(val) # remove first item with specified value
del a[-1] # Delete last element
del a[2:4] # Delete index 2 to 4(exclusive)
# Making Copies
arr[:] # Make copy of list
```

## Set
```javascript
var set = new Set()
// Adding
set.add(value)
// Deleting
set.clear()
set.delete(value)
// Checking Presence
set.has(value)
```
```python
set = set()
# Adding
set.add(item)
# Deleting
set.remove(item)
# Checking Presence
item in set
```

## Dict/Map
```javascript
var map = new Map();
// Getting
map.get(key)
map.keys() // get keys
map.size()
// Deleting
map.delete(key)
// Updating
map.set(key, []) // assign empty array to key
map.get(key).push(w) // Update array tied to key
// Checking Presence
map.has(key)
```
```python
map = {}
# Getting
map.get(key)
map.values()
map.keys()
# Deleting
map.pop(key)
# Updating
map.update({key : value})
map[key] = value
# Checking Presence
key in map
```

## String
```javascript
// ASCII code --> 96 to 122
char.charCodeAt() // Return ASCII code for char
String.fromCharCode(code) // Return the character given a ascii code
// Getting
str.indexOf("string", start) // Get index of where string was found from start
str.substring(start, endExclude)
str.length
// Conversion
arr.join('') // join array with delimiter to form string
str.split(" ") // Split string to form array
// Checking
str.includes('string')
```
```python
# a-z --> 97 to 122
# A-Z --> 65 to 90
ord(char) # Return ASCII code of char
chr(code) # Return character given ascii code
# Getting
len(string)
string.index(value)
string.find(value, start, end) # Get index of where string was found from start to end index
# Conversion
"#".join(arr) # join array with delimiter to form string
string.split(separator) # Split string to form array
# Checking
string.isalnum() # Alphanumeric
string.isalpha() # Alpha
string.isnumeric() # Numeric
string.islower() # Lowercase
string.isupper() # Uppercase
string.isspace() # Whitespace
```