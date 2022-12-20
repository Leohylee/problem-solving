// https://leetcode.com/problems/subsets/
//
// Given an integer array nums of unique elements, return all possible subsets (the power set).
//
// The solution set must not contain duplicate subsets. Return the solution in any order.

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode78_Subsets {

    public static void main(String[] args) {
        LeetCode78_Subsets solution = new LeetCode78_Subsets();
        System.out.println(solution.subsets(new int[]{1, 2, 3}));
    }

    private List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }

    private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        for(int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }

}