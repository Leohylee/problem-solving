public class LeetCode34_Find_First_and_Last_Position_of_Element_in_Sorted_Array {

    public static void main(String[] args) {
        LeetCode34_Find_First_and_Last_Position_of_Element_in_Sorted_Array_Solution solution = new LeetCode34_Find_First_and_Last_Position_of_Element_in_Sorted_Array_Solution();
        System.out.println(solution.searchRange(new int[]{5,6,7,7,8,8,8,8,8,8,10}, 8));
    }

}

class LeetCode34_Find_First_and_Last_Position_of_Element_in_Sorted_Array_Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[]{-1, -1};
        int pos = binarySearch(nums, target, 0, nums.length - 1);
        if (pos != -1) {
            ans[0] = pos;
            ans[1] = pos;
            while (ans[0] - 1 >= 0 && nums[ans[0] - 1] == target) {
                ans[0] = ans[0] - 1;
            }
            while (ans[1] + 1 < nums.length && nums[ans[1] + 1] == target) {
                ans[1] = ans[1] + 1;
            }
        }
        return ans;
    }

    public int binarySearch(int[] nums, int target, int l, int r) {
        if (l > r) return -1;
        int mid = (l + r) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] > target) {
            return binarySearch(nums, target, l, mid - 1);
        } else {
            return binarySearch(nums, target, mid + 1, r);
        }
    }
}
