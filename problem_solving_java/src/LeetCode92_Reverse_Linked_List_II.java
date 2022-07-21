import java.util.Stack;


public class LeetCode92_Reverse_Linked_List_II {

    public static void main(String[] args) {
        LeetCode92_Reverse_Linked_List_II_Solution solution = new LeetCode92_Reverse_Linked_List_II_Solution();
        ListNode_92 node = new ListNode_92(1, new ListNode_92(2 , new ListNode_92(3, new ListNode_92(4, new ListNode_92(5, new ListNode_92(6, new ListNode_92(7, new ListNode_92(8))))))));
        System.out.println(solution.reverseBetween_2(node, 3, 6));
    }

}

class LeetCode92_Reverse_Linked_List_II_Solution {
    public ListNode_92 reverseBetween(ListNode_92 head, int left, int right) {
        Stack stk = new Stack();
        ListNode_92 curr = head;
        ListNode_92 first = null;
        ListNode_92 last = null;
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
            curr = (ListNode_92) stk.pop();
            head = curr;
        } else {
            curr = first;
        }
        while(!stk.empty()) {
            curr.next = (ListNode_92) stk.pop();
            curr = curr.next;
        }
        curr.next = last;
        return head;
    }

    public ListNode_92 reverseBetween_2(ListNode_92 head, int m, int n) {
        ListNode_92 dummy = new ListNode_92(0);
        dummy.next = head;
        //first part
        ListNode_92 cur1 = dummy;
        ListNode_92 pre1 = null;
        for(int i=0;i<m;i++){
            pre1 = cur1;
            cur1 = cur1.next;
        }

        //reverse
        ListNode_92 cur2 = cur1;
        ListNode_92 pre2 = pre1;
        ListNode_92 q2;
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

class ListNode_92 {
    int val;
    ListNode_92 next;
    ListNode_92() {}
    ListNode_92(int val) { this.val = val; }
    ListNode_92(int val, ListNode_92 next) { this.val = val; this.next = next; }
}
