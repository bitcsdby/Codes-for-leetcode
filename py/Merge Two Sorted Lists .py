# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        p1 = l1;
        p2 = l2;
        
        l = None;
        
        if l1 == None:
            return l2;
        elif l2 == None:
            return l1;
        elif l1 == l2 == None:
            return None;
            
        if p1.val < p2.val:
            l = ListNode(p1.val);
            p1 = p1.next;
        else:
            l = ListNode(p2.val);
            p2 = p2.next;
        p = l;
        
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p.next = ListNode(p1.val);
                p = p.next;
                p1 = p1.next;
            else:
                p.next = ListNode(p2.val);
                p = p.next;
                p2 = p2.next;
        if p1 != None:
            count = p1;
            while p1 != None:
                p.next = ListNode(p1.val);
                p = p.next;
                p1 = p1.next;
        if p2 != None:
            while p2 != None:
                p.next = ListNode(p2.val);
                p = p.next;
                p2 = p2.next;
        
        return l;