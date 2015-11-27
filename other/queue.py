# 10.31.15


# queue implementation

class Queue():
    def __init__(self):
        self.i = []
        self.o = []
    def pop(self):
        if len(self.o) == 0:
            if len(self.i) == 0:
                return None
            while len(self.i) != 0:
                self.o.append(self.i.pop())
            return self.o.pop()
        return self.o.pop()
    def insert(self, x):
        self.i.append(x)

# classic implementation; to accommodate only singlely linked we pop at head
# and insert at tail
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    def pop(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            return temp.value
        return None
    def insert(self, x):
        nodex = node(x)
        if self.head == None:
            self.head = nodex
        if self.tail != None:
            self.tail.next = nodex
        self.tail = nodex

class node():
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def __str__(self):
        print self.value
