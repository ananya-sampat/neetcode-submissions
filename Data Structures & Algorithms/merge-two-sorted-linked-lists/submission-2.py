# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #start at the larger head value 
        #whichever head you took set the new head to be the next value
        #compare and continue
        '''
        curr1 = list1
        curr2 = list2

        if not curr1:
            return curr2
        if not curr2:
            return curr1

        if  curr1.val < curr2.val:
            head = curr1
            newlist = curr1
            curr1 = curr1.next
        else:
            head = curr2
            newlist = curr2
            curr2 = curr2.next 
        
        while curr1 and curr2:
            if curr1.val<curr2.val:
                newlist.next = curr1
                curr1 = curr1.next 
            else:
                newlist.next = curr2
                curr2 = curr2.next
            newlist = newlist.next
        
        if curr1:
            while curr1:
                newlist.next = curr1
                curr1= curr1.next 
                newlist = newlist.next
        if curr2:
            while curr2:
                newlist.next = curr2
                curr2 = curr2.next
                newlist = newlist.next
        return head
        '''
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next 
        curr.next = list1 if list1 else list2
        return dummy.next
                   