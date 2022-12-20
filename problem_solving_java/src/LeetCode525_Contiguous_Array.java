// https://leetcode.com/problems/contiguous-array/
//
// Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

import java.util.*;

public class LeetCode525_Contiguous_Array {

    public static void main(String[] args) {
        LeetCode525_Contiguous_Array solution = new LeetCode525_Contiguous_Array();
        System.out.println(solution.findMaxLength(new int[]{0,1}));
    }

    private int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int cnt = 0;
        int ans = 0;
        map.put(0,0);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                cnt--;
            } else {
                cnt++;
            }
            if (map.get(cnt) != null) {
                ans = Math.max(ans, i+1 - map.get(cnt));
            } else {
                map.put(cnt, i+1);
            }
        }
        return ans;
    }

}
