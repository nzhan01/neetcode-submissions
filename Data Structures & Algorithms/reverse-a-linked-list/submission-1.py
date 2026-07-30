# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #check if empty linked list
        if head == None:
            return head

        #iterate through linked list with 2 pointers. previous and current
        #while the current isn't null, we set current.next = previous
        # then we iterate by setting previous = current and 
        # current = original current.next stored in a temp variable
        
        current = head
        previous = None
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
    
        return previous