# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    node = ListNode(3, ListNode(2, ListNode(0)))
    node2 = ListNode(-4, node.next)
    node.next.next.next = node2
    print(solution.hasCycle(node))
