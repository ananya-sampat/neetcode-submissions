# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #go through list and add each pointer to a set of viewed pointers 
        # at each point check if the pointer is in the set
        # return true if it is 
        # if you hit null return false 
        seen = set()
        curr = head
        while curr:
            if curr not in seen:
                seen.add(curr)
                curr = curr.next
            if curr in seen:
                return True
        if  not curr:
                return False
        