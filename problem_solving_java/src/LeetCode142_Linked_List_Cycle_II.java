// https://leetcode.com/problems/linked-list-cycle-ii/
//
// Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
//
// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
// following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
// connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
//
// Do not modify the linked list.

public class LeetCode142_Linked_List_Cycle_II {

    public static void main(String[] args) {
        LeetCode142_Linked_List_Cycle_II solution = new LeetCode142_Linked_List_Cycle_II();
        ListNode node1 = solution.new ListNode(3);
        ListNode node2 = solution.new ListNode(2);
        ListNode node3 = solution.new ListNode(0);
        ListNode node4 = solution.new ListNode(-4);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node2;
        System.out.println(solution.detectCycle(node1));
    }

    //   Definition for singly-linked list.
    private class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    private ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (fast != slow) {
                    fast = fast.next;
                    slow = slow.next;
                }
                return slow;
            }
        }
        return null;
    }

}
