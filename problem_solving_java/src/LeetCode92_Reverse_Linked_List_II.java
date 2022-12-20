import java.util.Stack;


public class LeetCode92_Reverse_Linked_List_II {

    public static void main(String[] args) {
        LeetCode92_Reverse_Linked_List_II solution = new LeetCode92_Reverse_Linked_List_II();
        ListNode node = solution.new ListNode(1, solution.new ListNode(2, solution.new ListNode(3, solution.new ListNode(4, solution.new ListNode(5, solution.new ListNode(6, solution.new ListNode(7, solution.new ListNode(8))))))));
        System.out.println(solution.reverseBetween_2(node, 3, 6));
    }

    private class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    private ListNode reverseBetween(ListNode head, int left, int right) {
        Stack stk = new Stack();
        ListNode curr = head;
        ListNode first = null;
        ListNode last = null;
        int curr_pos = 1;
        while (curr != null) {
            if (curr_pos+1 == left) first = curr;
            if (left <= curr_pos && curr_pos <= right) {
                stk.push(curr);
                last = curr.next;
            }
            curr = curr.next;
            curr_pos++;
            if (curr_pos > right) break;
        }
        if (first == null && left == 1 && !stk.empty()) {
            curr = (ListNode) stk.pop();
            head = curr;
        } else {
            curr = first;
        }
        while(!stk.empty()) {
            curr.next = (ListNode) stk.pop();
            curr = curr.next;
        }
        curr.next = last;
        return head;
    }

    public ListNode reverseBetween_2(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        //first part
        ListNode cur1 = dummy;
        ListNode pre1 = null;
        for(int i=0;i<m;i++){
            pre1 = cur1;
            cur1 = cur1.next;
        }

        //reverse
        ListNode cur2 = cur1;
        ListNode pre2 = pre1;
        ListNode q2;
        for(int i=m;i<=n;i++){
            q2 = cur2.next;
            cur2.next = pre2;
            pre2 = cur2;
            cur2 = q2;
        }

        //connect
        pre1.next = pre2;
        cur1.next = cur2;

        return dummy.next;
    }

}
