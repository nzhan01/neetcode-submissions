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

        #iterate through linked list with 2 pointers
        #at each index, swap indexes
        #similar to bubble sort where first element will get pushed to end
        
        current = head
        previous = None
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
    
        return previous