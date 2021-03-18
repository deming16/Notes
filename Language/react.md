# React

## Why use React?

## What is a key in react and its purpose
These are identifiers given to things usually in an array so that react can track if that item has changes if its changes with the state if its change with the component, whenever you have a list of items and if one of those items changes react needs to know about it and you have to give it a key to each one of those items normally you can use it like an ID with an incremented number on it, it would be like ... list item number 1 ... list item number two .. list number three ..etc . They need to be unique identifier

## Differences between stateful and stateless component?
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

## Life Cycle Hooks
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

## why use arrow functions in react?
In react, we can have onClick handlers, which is not actually a class method but a class property