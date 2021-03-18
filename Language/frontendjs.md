# Frontend JavaScript

## Hoisting
Hoisting is a term used to explain the behavior of variable declarations in your code. Variables declared or initialized with the var keyword will have their declaration "moved" up to the top of their module/function-level scope, which we refer to as hoisting. However, only the declaration is hoisted, the assignment (if there is one), will stay where it is.

Note that the declaration is not actually moved - the JavaScript engine parses the declarations during compilation and becomes aware of declarations and their scopes. It is just easier to understand this behavior by visualizing the declarations as being hoisted to the top of their scope. Let's explain with a few examples.

```javascript
console.log(foo); // undefined
var foo = 1;
console.log(foo); // 1
```

Function declarations have the body hoisted while the function expressions (written in the form of variable declarations) only has the variable declaration hoisted.

```javascript
// Function Declaration
console.log(foo); // [Function: foo]
foo(); // 'FOOOOO'
function foo() {
  console.log('FOOOOO');
}
console.log(foo); // [Function: foo]

// Function Expression
console.log(bar); // undefined
bar(); // Uncaught TypeError: bar is not a function
var bar = function () {
  console.log('BARRRR');
};
console.log(bar); // [Function: bar]
```
Variables declared via let and const are hoisted as well. However, unlike var and function, they are not initialized and accessing them before the declaration will result in a ReferenceError exception. The variable is in a "temporal dead zone" from the start of the block until the declaration is processed.
```javascript
x; // undefined
y; // Reference error: y is not defined

var x = 'local';
let y = 'local';
```
## var/let/const
Scoping - var (global/function scope)
let, const (block scoping)
const cannot be reassigned, but can be changed

## Promises
promises - Object that may produce a value sometime in the future
promises has 3 states - fufilled, rejected pending
## async/await
## callbacks
## observables - rxjs

## Closures
inheritance vs ES6 classes, crane?

## call/bind/apply

## DOM
```javascript
body.append() // can be multiple thing and string
body.appendChild() // only one thing and cannot be string
document.createElement('div') create div

div.innerText = "Hello World" // only presents text that are visible
div.textContent = "Hello World" // shows text even when not visible, just like in html

document.getElementsById()
document.getElementByClassName()
document.querySelector('div') // select div
document.querySelector('#hi') // select tags with id hi
div.remove() // remove the element, but div is still kept
div.getAttribute(); div.setAttribute(); div.removeAttribute() // get and set attribute
div.classList.add/remove/toggle()
div.style.backgroundColor
```
### Event Listeners
Event listeners from child will bubble up
```javascript
e.stopPropgation()
e.target.match("div") // get divs of the target
div.addEventListener('click', e => {
  // execute code
})
```

## Debounce
```javascript
function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}
function saveInput(){
  console.log('Saving data');
}
const processChange = debounce(() => saveInput());

<input type="text" onkeyup="processChange()" />
```

## Debounce_leading
```javascript
function debounce_leading(func, timeout = 300){
  let timer;
  return (...args) => {
    if (!timer) {
      func.apply(this, args);
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = undefined;
    }, timeout);
  };
}
```