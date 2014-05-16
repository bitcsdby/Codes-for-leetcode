# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head== None: #空集
            return None;
        if head.next == None: #单节点
            return head;
            
        p = head;
        count = 0;
        
        tmphead = p.next;
        tmp = p.next.next;
        p.next.next=p;
        p.next = tmp;
        head = tmphead;
        
        if p == None:
            return head;
        p = head.next;
        
        while p.next != None:
            if p.next.next == None:
                break;
                
            tmp = p.next.next;
            p.next.next = tmp.next;
            tmp.next = p.next;
            p.next = tmp;
            
            p = p.next.next;
            if p == None:
                break;
                
        return head;
                
            
            