# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        #split in half 
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        #switch the order of the second list
        newhead = slow.next 
        
        stack = []
        stack.append(slow)
        while slow.next:
            slow = slow.next 
            stack.append(slow)
        newhead=stack.pop()
        slow = newhead
        while stack:
            slow.next = stack.pop()
            slow = slow.next
        slow.next = None
        #combine 
        curr = head
        slow = newhead

        while slow and curr:
            temp1 = curr.next
            temp2 = slow.next

            curr.next = slow
            slow.next = temp1

            curr = temp1
            slow = temp2

                
                