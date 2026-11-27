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
        '''
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
        '''
        '''
        #Floyd's Algorithm
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False 
        '''
        slow = fast = head
        def helper(slow,fast):
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
            if fast:
                return helper(slow, fast)
            return False
        return helper(slow,fast)
        
