from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count the total length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # Determine the size of each part
        part_size = length // k
        extra = length % k

        result = []
        node = head

        for i in range(k):
            part_head = node
            curr_part_size = part_size + (1 if i < extra else 0)
            for j in range(curr_part_size - 1):
                if node:
                    node = node.next
            if node:
                next_part = node.next
                node.next = None
                node = next_part
            result.append(part_head)

        return result
