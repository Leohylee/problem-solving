# https://leetcode.com/problems/sort-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, slow, fast = None, head, head
        while (fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)


    def merge(self, left, right):
        head = ListNode(0)
        curr = head
        while left and right:
            if left.val < right.val:
                curr.next = left
                curr = curr.next
                left = left.next
            else:
                curr.next = right
                curr = curr.next
                right = right.next
        while left:
            curr.next = left
            curr = curr.next
            left = left.next
        while right:
            curr.next = right
            curr = curr.next
            right = right.next
        return head.next



if __name__ == "__main__":
    solution = Solution()
    node = ListNode(4, ListNode(1, ListNode(2, ListNode(3))))
    print(solution.sortList(node))
