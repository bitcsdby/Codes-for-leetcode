# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False;
        step1 = head;
        step2 = head.next;
        
        while step1 != None and step2 != None:
            if step1 == step2:
                return True;
            if step1.next != None:
                step1 = step1.next;
            else:
                break;
            if step2.next != None:
                step2 = step2.next;
            else:
                break;
            if step2.next != None:
                step2 = step2.next;
            else:
                break;
        return False;
        