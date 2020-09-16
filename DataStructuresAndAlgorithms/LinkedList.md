# 1. Removal of Nodes in Linked List
## Remove Linked List Elements
```
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # Having a dummy head will deal with edge 
        # case head being the one being removed
        dummy_head = ListNode(-1)
        dummy_head.next = head
        currNode = dummy_head
        
        while currNode.next != None:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        
        return dummy_head.next
```

## Remove Duplicates from Sorted List
```
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy_head = ListNode('a')
        dummy_head.next = head
        currNode = dummy_head
        
        while currNode.next != None:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next
        
        return dummy_head.next
```

# 2. Reverseal of Linked List
## Reverse Linked List
```
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        
        return prev
```

# 3. Merging Linked List
## Merge Two Sorted Lists
```
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```
```python 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        L1 = l1
        L2 = l2
        curr = dummy
        
        while L1 != None and L2 != None:
            print(L1.val, L2.val)
            if L1.val < L2.val:
                curr.next = L1
                L1 = L1.next
            else:
                curr.next = L2
                L2 = L2.next
            curr = curr.next
        
        if L1 != None:
            curr.next = L1
        else:
            curr.next = L2
        
        return dummy.next
```