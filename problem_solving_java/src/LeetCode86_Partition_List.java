public class LeetCode86_Partition_List {

    public static void main(String[] args) {
        LeetCode86_Partition_List solution = new LeetCode86_Partition_List();
        ListNode node = solution.new ListNode();
        System.out.println(solution.partition(node, 0));
    }

    private class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    private ListNode partition(ListNode head, int x) {
        ListNode big = new ListNode(0), small = new ListNode(0);
        ListNode startB = big, startS = small;
        while (head != null) {
            ListNode temp = new ListNode(head.val);
            if (head.val < x) {
                small.next = temp;
                small = small.next;
            } else {
                big.next = temp;
                big = big.next;
            }
            head = head.next;
        }
        big.next = null;
        small.next = startB.next;
        return startS;
    }

}
