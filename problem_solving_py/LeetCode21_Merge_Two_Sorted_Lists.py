# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        ans = head
        while list1 and list2:
            if list1.val > list2.val:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            ans = ans.next
        while list1:
            ans.next = list1
            ans = ans.next
            list1 = list1.next
        while list2:
            ans.next = list2
            ans = ans.next
            list2 = list2.next
        return head.next



if __name__ == "__main__":
    solution = Solution()
    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    print(solution.mergeTwoLists(node1, node2))
