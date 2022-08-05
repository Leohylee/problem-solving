public class LeetCode378_Kth_Smallest_Element_in_a_Sorted_Matrix {

    public static void main(String[] args) {
        LeetCode378_Kth_Smallest_Element_in_a_Sorted_Matrix_Solution solution = new LeetCode378_Kth_Smallest_Element_in_a_Sorted_Matrix_Solution();
        System.out.println(solution.kthSmallest(new int[][]{{1,5,9},{10,11,13},{12,13,15}}, 8));
    }

}

class LeetCode378_Kth_Smallest_Element_in_a_Sorted_Matrix_Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int l = matrix[0][0], r = matrix[matrix.length-1][matrix[0].length-1];
        int ans = -1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (countLessOrEqual(matrix, m) >= k) {
                ans = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return ans;
    }

    private int countLessOrEqual(int[][] matrix, int x) {
        int cnt = 0;
        for (int r = 0; r < matrix.length; r++) {
            int c = matrix[r].length - 1;
            while (c >= 0 && matrix[r][c] > x) c--;
            cnt += c + 1;
        }
        return cnt;
    }
}
