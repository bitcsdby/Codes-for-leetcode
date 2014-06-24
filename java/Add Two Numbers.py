# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        p1 = l1
        p2 = l2
        c = 0
        
        while True:
            p1.val = p1.val+p2.val+c
            if p1.val >= 10:
                p1.val %= 10
                c = 1
            else:
                c = 0
            p2.val = p1.val
            if p1.next == None or p2.next == None:
                break
            p1 = p1.next
            p2 = p2.next    
            
        if p1 != None and p1.next != None:    
            p1 = p1.next
            while p1.next != None:
                p1.val += c
                if p1.val >= 10:
                    p1.val %= 10
                    c = 1
                else:
                    c = 0
                p1 = p1.next
            p1.val += c
            if p1.val >= 10:
                p1.next = ListNode(1)
                p1.val = 0
                
            return l1
            
        if p2 != None and p2.next != None:
            p2 = p2.next
            while p2.next != None:
                p2.val += c
                if p2.val >= 10:
                    p2.val %= 10
                    c = 1
                else:
                    c = 0
                p2 = p2.next
            p2.val += c
            if p2.val >= 10:
                p2.next = ListNode(1)
                p2.val = 0
            
            return l2
            
        if c == 1:
            p1.next = ListNode(1)
            p1.val %= 10
        return l1