class LinkNode:
    def __init__(self, key,value):
        self.key = key
        self.val = value
        self.next = None
        self.pre = None
        
class LRUCache:
    def tohead(self,head,p):
        if head == p:
            return head;
            
        if p == self.last:
            self.last = p.pre
        p.pre.next = p.next;
        if p.next != None:
            p.next.pre = p.pre
        tmphead = head
        head = p
        p.pre = None;
        p.next = tmphead;
        tmphead.pre = p
    return head
    
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = None
        self.last = None
        self.vol = 0

    def get(self, key):
        if self.cache.has_key(key) and self.cache[key] != None:
                if self.head != self.cache[key]:
                    self.head = self.tohead(self.head,self.cache[key])
                return self.cache[key].val

        return -1;

    def set(self, key, value):
        if self.cache.has_key(key) and self.cache[key] != None:
            self.cache[key].val = value
            if self.head != self.cache[key]:
                if self.head != self.cache[key]:
                    self.head = self.tohead(self.head,self.cache[key])
            return 
        if self.vol < self.cap:   #insert new
            self.vol += 1
            tmp = LinkNode(key,value)
            if self.vol == 1:
                self.last = tmp
            else:
                self.head.pre = tmp
            self.cache[key] = tmp
            tmp.next = self.head
            tmp.pre = None;
            self.head = tmp;

        else:
            if self.last == self.head:
                self.cache[self.last.key] = None;
                self.head = None
                self.last = None
            else:
                self.cache[self.last.key] = None;
                tmp = self.last
                self.last = self.last.pre
                self.last.next = None;
                tmp = None;

            tmp = LinkNode(key,value)
            self.cache[key] = tmp
            if self.head != None:
            self.head.pre = tmp
            tmp.next = self.head;
            tmp.pre = None;
            self.head = tmp;
        return  #last pointer has problem