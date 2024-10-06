def movePointer(head, diff):
    while diff:
        head = head.next
        diff -= 1

    return head
