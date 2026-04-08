class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = None

a = Node(0)
head = a
b = Node(5)
c = Node(10)
d = Node(15)
e = Node(20)
a.next = b
b.next = c
c.next = d
d.next = e

l = 0
n = 5
curr = head
while curr:
    curr = curr.next
    l += 1

if l == n:
    newhead = head.next
    del head
    print(newhead.val)