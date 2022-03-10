# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ext = 0
        head = ListNode(0, None)
        ans = head
        while l1 and l2:
            sum, ext = self.sumValues(l1.val, l2.val, ext)
            ans.next = ListNode(sum)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sum, ext = self.sumValues(l1.val, 0, ext)
            ans.next = ListNode(sum)
            ans = ans.next
            l1 = l1.next
        while l2:
            sum, ext = self.sumValues(l2.val, 0, ext)
            ans.next = ListNode(sum)
            ans = ans.next
            l2 = l2.next
        if ext != 0:
            ans.next = ListNode(ext)
        return head.next

    def sumValues(self, a=0, b=0, c=0):
        ext = 0
        ans = a + b + c
        if len(str(ans)) > 1:
            ans, ext = int(str(ans)[1]), int(str(ans)[0])
        return ans, ext


if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    node2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(solution.addTwoNumbers(node1, node2))
