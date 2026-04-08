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

prev = None
curr = head

while curr != None:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
head = prev
# print the list

while head != None:
    print(head.val, end=",")
    head = head.next