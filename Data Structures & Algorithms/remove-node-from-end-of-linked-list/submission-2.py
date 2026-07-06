# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        dummy = ListNode()
        skip = len(nodes) - n

        if skip == 0:
            dummy.next = nodes[skip].next
        elif skip > 0:
            dummy.next = nodes[0]
            nodes[skip-1].next = nodes[skip].next

        return dummy.next
            
