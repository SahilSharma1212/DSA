class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


a = Node(5)
b = Node(10)
c = Node(15)

a.next = b
b.next = c

head = a


tail = a
while tail.next != None:
    tail = tail.next

tail.next = Node(20)

while head != None:
    print(head.val)
    head = head.next