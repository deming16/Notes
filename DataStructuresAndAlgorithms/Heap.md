## Heap Construction
```
Implement a MinHeap class that supports:
  - Building a Min Heap from an input array of integers
  - Inserting integers in the heap
  - Removing the heap's minimum / root value
  - Peeking at the heap's minimum / root value
  - Sifting integers up and down the heap, which is to be used when inserting and removing values

  Note that the heap should be represented in the form of an array.
```
```python
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
	# currentNode -> i
	# childOne -> 2i + 1
	# childTwo -> 2i + 2
	# parentNode -> floor((i-1) / 2)
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
		lastParentIdx = (len(array) - 2) // 2
		for currIdx in reversed(range(lastParentIdx + 1)):
			self.siftDown(currIdx, len(array) - 1, array)
        return array

    def siftDown(self, currIdx, endIdx, heap):
		childOneIdx = currIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
			# Choose the smaller child to decide whether to swap
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				swapIdx = childTwoIdx
			else:
				swapIdx = childOneIdx
			# Decide whether to swap
			if heap[currIdx] > heap[swapIdx]:
				heap[currIdx], heap[swapIdx] = heap[swapIdx], heap[currIdx]
				currIdx = swapIdx
				childOneIdx = currIdx * 2 + 1
			else:
				return

    def siftUp(self, currIdx, heap):
		parentIdx = (currIdx - 1) // 2
		while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
			heap[currIdx], heap[parentIdx] = heap[parentIdx], heap[currIdx]
			currIdx = parentIdx
			parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
		heap = self.heap
        heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
		valueToRemove = heap.pop()
		self.siftDown(0, len(heap) - 1, heap)
		return valueToRemove

    def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
```


## Continuous Median
```
Write a ContinuousMedianHandler class that supports:
  - The continuous insertion of numbers with the insert method.
  - The instant O(1) retrieval of the median of the numbers that have been inserted thus far with the getMedian method.

If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle(3 in this case); if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the two middle numbers ( (3 + 7) / 2 == 5 in this case)
```
```python
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
		self.lowerHalf = []
		self.greaterHalf = []

	def siftUp(self, currIdx, heap, heapType):
		parentIdx = (currIdx - 1) // 2
		while currIdx > 0:
			if heapType == 'min':
				if heap[currIdx] < heap[parentIdx]:
					heap[currIdx], heap[parentIdx] = heap[parentIdx], heap[currIdx]
					currIdx = parentIdx
					parentIdx = (currIdx - 1) // 2
				else:
					return
			else:
				if heap[currIdx] > heap[parentIdx]:
					heap[currIdx], heap[parentIdx] = heap[parentIdx], heap[currIdx]
					currIdx = parentIdx
					parentIdx = (currIdx - 1) // 2
				else:
					return
	
	def siftDown(self, currIdx, endIdx, heap, heapType):
		childOneIdx = currIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1:
				if heapType == 'min':
					if heap[childOneIdx] < heap[childTwoIdx]:
						idxToSwap = childOneIdx
					else:
						idxToSwap = childTwoIdx
				else:
					if heap[childOneIdx] > heap[childTwoIdx]:
						idxToSwap = childOneIdx
					else:
						idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			
			if heapType == 'min':
				if heap[idxToSwap] < heap[currIdx]:
					heap[idxToSwap], heap[currIdx] = heap[currIdx], heap[idxToSwap]
					currIdx = idxToSwap
					childOneIdx = currIdx * 2 + 1
				else:
					return
			else:
				if heap[idxToSwap] > heap[currIdx]:
					heap[idxToSwap], heap[currIdx] = heap[currIdx], heap[idxToSwap]
					currIdx = idxToSwap
					childOneIdx = currIdx * 2 + 1
				else:
					return
	
	def remove(self, heap, heapType):
		heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
		valueToRemove = heap.pop()
		self.siftDown(0, len(heap) - 1, heap, heapType)
		return valueToRemove
		
    def insert(self, number):
		# If lower half is empty or number belongs to lower half,
		# insert to lower else greater
		if len(self.lowerHalf) == 0 or number < self.lowerHalf[0]:
			self.lowerHalf.append(number)
			self.siftUp(len(self.lowerHalf) - 1, self.lowerHalf, 'max')
		else:
			self.greaterHalf.append(number)
			self.siftUp(len(self.greaterHalf) - 1, self.greaterHalf, 'min')
		
		# Balance the heap
		if len(self.lowerHalf) - len(self.greaterHalf) == 2:
			self.greaterHalf.append(self.remove(self.lowerHalf, 'max'))
			self.siftUp(len(self.greaterHalf) - 1, self.greaterHalf, 'min')
		elif len(self.greaterHalf) - len(self.lowerHalf) == 2:
			self.lowerHalf.append(self.remove(self.greaterHalf, 'min'))
			self.siftUp(len(self.lowerHalf) - 1, self.lowerHalf, 'max')
			
		# Update the median
		if len(self.lowerHalf) == len(self.greaterHalf):
			# total length is even
			self.median = (self.lowerHalf[0] + self.greaterHalf[0]) / 2
		# total length is odd
		elif len(self.lowerHalf) > len(self.greaterHalf):
			self.median = self.lowerHalf[0]
		else:
			self.median = self.greaterHalf[0]

    def getMedian(self):
        return self.median
```