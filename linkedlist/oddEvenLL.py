class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# create nodes
n1 = ListNode(0)
n2 = ListNode(5)
n3 = ListNode(10)
n4 = ListNode(15)
n5 = ListNode(20)

# connect nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# head of linked list
head = n1

if not head:
    print("empty list")

odd = head
even = head.next
evest = even

while even and even.next:
    # connect odd
    odd.next = even.next
    odd = odd.next

    # connect even
    even.next = odd.next
    even = even.next

# connect both lists
odd.next = evest
