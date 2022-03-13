# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        curr = head
        cnt = 0
        while curr:
            cnt = cnt + 1
            curr = curr.next
        if k % cnt > 0:
            keep = cnt - k % cnt - 1
            head = self.rotate(head, keep)
        return head

    def rotate(self, head: Optional[ListNode], keep: int):
        curr = head
        while keep > 0:
            curr = curr.next
            keep = keep - 1
        oldhead = head
        head = curr.next
        curr.next = None
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = oldhead
        return head



if __name__ == "__main__":
    solution = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, ListNode(11)))))))))))
    print(solution.rotateRight(node, 0))
