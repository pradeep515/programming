def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2
    while current1 != current2:
        current1 = current1.next if current1 else head2
        current2 = current2.next if current2 else head1
    return current1.data


