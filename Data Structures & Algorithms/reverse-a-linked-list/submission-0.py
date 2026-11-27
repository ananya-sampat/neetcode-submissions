# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #go to the end of the list where the next pointer is null
        #at each point add the pointers to a list 
        #once at the end set the end to the head and the next pointer to whatever pops out of the stack 
        #continue until the stack is empty 
        if not head:
            return None
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        head = stack.pop()
        curr = head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None

        return head