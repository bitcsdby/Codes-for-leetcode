class Solution:

    def merge(self,left,right):
        p = left
        q = right
        head = ListNode(0)
        n = head
        
        
        while p != None and q != None:
            if p.val > q.val:
                n.next = q
                q = q.next
                n = n.next
                n.next = None
            else:
                n.next = p
                p = p.next
                n = n.next
                n.next = None
        while p != None:
            n.next = p
            p = p.next
            n = n.next
        
        while q != None:
            n.next = q
            q = q.next
            n = n.next
            

        return head.next
                
        
    def sortit(self,head): 
        if head.next == None:
            return head
            
        p = head.next
        q = head
        l = 0
        
        while p != None:
            p = p.next
            if p != None:
                p = p.next
            else:
                break
            q = q.next
        
        p = q
        q = q.next
        p.next = None
        left = self.sortit(head)
        right = self.sortit(q)
        
        return self.merge(left,right)
        
    def sortList(self, head):
        if head == None:
            return None;
        
        p = head

        return self.sortit(head)