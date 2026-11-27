# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # stack of all pointers
        stack = []
        # pop n pointers and recieve the last one 
        stack.append(head)
        temp = head
        while temp.next:
            stack.append(temp.next)
            temp = temp.next
        for i in range(n):
            temp = stack.pop()
        if stack:
            curr = stack.pop()
            curr.next = temp.next
        else:
            return head.next
        return head

        
        


         


        