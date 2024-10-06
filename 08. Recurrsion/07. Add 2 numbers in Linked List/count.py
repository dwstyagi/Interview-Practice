def count(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next

    return count
