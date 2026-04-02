# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Input = linked list
        # Output = re-ordered linked list (not returning)
        # [0, n-1, 1, n-2, 2, n-3, ...]
        # First node stays in place, first.next = n-1, second node, second.next = n-2, ith.next = n-i

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        # merge two halves
        first, second = head, prev # new head of second half
        while second:
            # when breaking links, store next nodes in tmp
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



