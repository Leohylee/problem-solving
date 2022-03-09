# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode(-999999, head)
        curr = head.next
        while curr:
            curr = self.checkVal(curr.val, curr)
            tail.next = curr
            tail = curr
            curr = curr.next if curr else None
        return head.next

    def checkVal(self, val: int, node: Optional[ListNode]):
        nextNode = node.next if node else None
        if nextNode == None or nextNode.val != val:
            return node
        else:
            while nextNode and nextNode.val == val:
                nextNode = nextNode.next
            nextNode = self.checkVal(nextNode.val if nextNode else 0, nextNode)
            return nextNode

#     public ListNode deleteDuplicates(ListNode head) {
#     if (head == null) return null;
#
#     if (head.next != null && head.val == head.next.val) {
#         while (head.next != null && head.val == head.next.val) {
#             head = head.next;
#         }
#         return deleteDuplicates(head.next);
#     } else {
#         head.next = deleteDuplicates(head.next);
#     }
#     return head;
# }

if __name__ == "__main__":
    solution = Solution()
    node = ListNode(1, ListNode(1))
    print(solution.deleteDuplicates(node))
