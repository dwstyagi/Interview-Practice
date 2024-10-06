from node import Node


def extraList(biggerHead, tempBiggerHead, carry, result):
    if biggerHead == tempBiggerHead:
        return result

    nextNode = extraList(biggerHead.next, tempBiggerHead, carry, result)

    total = biggerHead.data + carry[0]
    data = total % 10
    carry[0] = total // 10

    currentNode = Node(data)
    currentNode.next = nextNode

    return currentNode
