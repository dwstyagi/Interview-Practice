class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, node):
    if head == None:
        head = node
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = node
    return head


def count(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next

    return count


def printList(head):
    if head == None:
        return None
    else:
        temp = head
        while temp.next:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)
