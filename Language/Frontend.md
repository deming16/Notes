# Frontend

## CSS

### How to do selectors
```css
div.red.green /* select div with class of red and green */
span, li /* spans and li are selected */
ul li /* select li inside of a ul, even if it grand children */
ul > li /* select li that is direct child of ul */
li.red ~ li /* select li that comes after li with class red */
li.red + li /* select just the li that is directly after li with class red
```
### nth element selectors
```css
li.red:first-child /* select the very first child that is li with .red (must be first)*/
li:nth-child()
```
### Box Sizing
css box sizing - border box (account for border and padding etc when specifying sizes)

## JavaScript

### Hosting
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
### var/let/const
Scoping - var (global/function scope)
let, const (block scoping)
const cannot be reassigned, but can be changed

### Promises
promises - Object that may produce a value sometime in the future
promises has 3 states - fufilled, rejected pending
### async/await
### callbacks
### observables - rxjs

### Closures
inheritance vs ES6 classes, crane?

### call/bind/apply

## React

### Why use React?

### What is a key in react and its purpose
These are identifiers given to things usually in an array so that react can track if that item has changes if its changes with the state if its change with the component, whenever you have a list of items and if one of those items changes react needs to know about it and you have to give it a key to each one of those items normally you can use it like an ID with an incremented number on it, it would be like ... list item number 1 ... list item number two .. list number three ..etc . They need to be unique identifier

### Differences between stateful and stateless component?
*Stateful component* 

1. Stores info about component's state changes in memory 
2. Have authority to change state 
3. Contain the knowledge of past, current and possible future changes in state
4. Stateless component notify them about the requirement of the state change, then they send down the props to them 

*Stateless component* 

1. Calculates the internal state of the components 
2. Do not have the authority to change state  
3. Contain no knowledge of past, current and possible future state changes
4. They receive the props from the stateful components and treat them as callback functions

### Life Cycle Hooks
React - componentDidMount
- life cycle methods are changing
- there are initial render and re-render with diff lifecycles methods

1. constructor - run only once to set initialState only place to  use this.state
2. getDerivedStateFromProps- runs after constructor (has inital and rerender)
 - when props change, set the state accordingly
 - static because dont want user to access 'this'
 - returns newState or null
3. render - return the jsx, mandatory
 - cannot set state here
4. componentDidMount - when use 3rd party library need to wait under dom is ready


rerender
1. static getDerivedStateFromProps
2. shouldComponentUpdate
  - need to decide if the component need to be updated or not
  - every set state cause the whole component to re render
  - but some parts could be setting the same state
  - compare prev and new state and return true or false
3. render
4. getSnapshotBeforeUpdate
  - to do something before render
5. componentDidUpdate

When component dies
componentWillUnmount - to do before unmount

### why use arrow functions in react?
In react, we can have onClick handlers, which is not actually a class method but a class property

### DOM
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