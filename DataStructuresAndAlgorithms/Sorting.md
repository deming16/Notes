## Bubble Sort
```python
def bubbleSort(array):
    # Write your code here.
	isSorted = False
	counter = 0
	while isSorted == False:
		isSorted = True
		for i in range(len(array) - 1 - counter):
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				isSorted = False
		
		counter += 1
	
	return array
    pass
```

## Insertion Sort
```python
def insertionSort(array):
    # Write your code here.
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j - 1]:
			array[j], array[j-1] = array[j - 1], array[j]
			j -= 1
	
	return array
    pass
```

## Selection Sort
```python
def selectionSort(array):
    # Write your code here.
	currIdx = 0
	while currIdx < len(array) - 1:
		smallestIdx = currIdx
		smallest = float("inf")
		for i in range(currIdx, len(array)):
			if array[i] < smallest:
				smallest = array[i]
				smallestIdx = i
		
		array[smallestIdx], array[currIdx] = array[currIdx], array[smallestIdx]
		currIdx += 1
	
	return array
    pass
```

## Quick Sort
```python
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(left, right, array)
		if array[left] <= array[pivot]:
			left += 1
		if array[right] >= array[pivot]:
			right -= 1
	
	swap(start, right, array)
	quickSortHelper(array, start, right - 1)
	quickSortHelper(array, right + 1, end)
		

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
```