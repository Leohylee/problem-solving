# https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide(lists):
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]
            return self.merge(divide(left), divide(right))

        if not lists:
            return None
        return divide(lists)

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2


if __name__ == "__main__":
    solution = Solution()
    list_node = [ListNode(1, ListNode(4, ListNode(5, None))), ListNode(1, ListNode(3, ListNode(4, None))), ListNode(2, ListNode(6, None))]
    print(solution.mergeKLists(list_node))
