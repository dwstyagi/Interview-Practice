from count import count


def calcDifference(head1, head2):
    totalNodesInList1 = count(head1)
    totalNodesInList2 = count(head2)

    if totalNodesInList1 < totalNodesInList2:
        biggerList = head2
    else:
        biggerList = head1

    return [abs(totalNodesInList1 - totalNodesInList2), biggerList]
