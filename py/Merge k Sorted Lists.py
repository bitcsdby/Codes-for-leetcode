# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        sortlist = []
        
        for x in lists:
            p = x
            while p != None:
                sortlist.append(p)
                p = p.next
                
        sortlist.sort(key=lambda x:x.val)
        
        head = ListNode(1)
        p = head
        
        for x in sortlist:
            p.next = x
            p = p.next
        
        return head.next