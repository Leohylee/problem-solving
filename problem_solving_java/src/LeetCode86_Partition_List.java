public class LeetCode86_Partition_List {

    public static void main(String[] args) {
        LeetCode86_Partition_List_Solution solution = new LeetCode86_Partition_List_Solution();
        ListNode_86 node = new ListNode_86();
        System.out.println(solution.partition(node, 0));
    }

}

class LeetCode86_Partition_List_Solution {
    public ListNode_86 partition(ListNode_86 head, int x) {
        ListNode_86 big = new ListNode_86(0), small = new ListNode_86(0);
        ListNode_86 startB = big, startS = small;
        while (head != null) {
            ListNode_86 temp = new ListNode_86(head.val);
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

class ListNode_86 {
    int val;
    ListNode_86 next;
    ListNode_86() {}
    ListNode_86(int val) { this.val = val; }
    ListNode_86(int val, ListNode_86 next) { this.val = val; this.next = next; }
}
