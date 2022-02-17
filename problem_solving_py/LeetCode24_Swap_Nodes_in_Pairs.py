# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        tail = head.next
        head.next = self.swapPairs(tail.next)
        tail.next = head
        return tail


if __name__ == "__main__":
    solution = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    print(solution.swapPairs(node))
