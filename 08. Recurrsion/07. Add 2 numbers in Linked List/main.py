from node import Node, insert, printList, count
from diff import calcDifference
from move import movePointer
from util import addTwoNumbersUtil
from extraList import extraList


def addNumbers(head1, head2):
    carry = [0]

    diff = calcDifference(head1, head2)[0]
    biggerHead = calcDifference(head1, head2)[1]

    smallerHead = head1 if biggerHead == head2 else head2

    equalHead = movePointer(biggerHead, diff)

    result = addTwoNumbersUtil(equalHead, smallerHead, carry)

    head = result

    if diff:
        head = extraList(biggerHead, equalHead, carry, result)

    if carry[0]:
        node = Node(carry[0])
        node.next = head
        head = node

    return head


L1 = None
for i in [8, 5, 8]:
    L1 = insert(L1, Node(i))

L2 = None
for i in [5, 6, 4]:
    L2 = insert(L2, Node(i))

node = addNumbers(L1, L2)

printList(node)
# print(node)
