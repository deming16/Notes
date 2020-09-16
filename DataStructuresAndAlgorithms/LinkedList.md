# Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
```
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