# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        rethead = None;
        if head == None:
            return None;
        
        p = head;
        max = p.val
        rethead = ListNode(-1);
        rethead.next = p
        lastnode = p;
        
        head = p.next;
        p.next = None;
        p = head;
        
        while p != None:
            if p.val > max: #append
                max = p.val;
                lastnode.next = p;
                lastnode = lastnode.next;
                tmpp = p.next
                p.next = None
                p = tmpp
                continue;
            q = rethead;
            while q.next != None and q.next.val < p.val:
                q = q.next;
            tmpp = p.next
            tmp = q.next;
            q.next = p
            p.next = tmp;
            p = tmpp;
            
        return rethead.next