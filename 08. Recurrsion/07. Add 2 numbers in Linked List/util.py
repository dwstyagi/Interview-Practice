from node import Node


def addTwoNumbersUtil(head1, head2, carry):

    if head1.next is None and head2.next is None:
        total = head1.data + head2.data
        data = total % 10
        carry[0] = total // 10
        return Node(data)

    nextNode = addTwoNumbersUtil(head1.next, head2.next, carry)

    total = head1.data + head2.data + carry[0]
    data = total % 10
    carry[0] = total // 10

    currentNode = Node(data)
    currentNode.next = nextNode

    return currentNode
