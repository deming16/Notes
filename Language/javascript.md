# JavaScript
```javascript
// Ternery
a = condition ? valueWhenTrue : valueWhenFalse;
// Absolute 
a = Math.abs(value)
// Integer Division
Math.floor(y/x)
Infinity // Max number
```

## For Loops
```javascript
for (let i = 0; i < limit; i++){
  // CODE HERE...
}
for (let i of array) {
  // i is the element in the array
}
```

## Array
```javascript
arr.length // length of array
Array.isArray(arr) // Check if item is of type array
Array(R).fill().map(() => Array(C).fill(false)) // Init 0/false for matrix
Array(R).fill(0) // init 0/false for array

// OPERATIONS
arr.sort() // Sort in desc
arr.sort((a, b) => a - b) // Sort in asc 
arr.slice(x, y) // return array from index [x, y), array.slice() to make a copy
arr.concat(arr1) // concat 2 arrays
arr.reverse() // reverse array
arr.push() // add element to end of array
arr.pop() // pop element from end of array
arr.shift() // remove first element
```

## Strings
```javascript
// ASCII code --> 96 to 122
char.charCodeAt() // Return ASCII code for char

String.fromCharCode(code) // Return the character given a ascii code
arr.join('') // join array with delimiter
str.includes('string')
parseInt(str)
```