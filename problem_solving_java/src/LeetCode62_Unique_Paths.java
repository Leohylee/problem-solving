public class LeetCode62_Unique_Paths {

    public static void main(String[] args) {
        LeetCode62_Unique_Paths_Solution solution = new LeetCode62_Unique_Paths_Solution();
        System.out.println(solution.uniquePaths(3, 7));
    }

}

class LeetCode62_Unique_Paths_Solution {
    public int uniquePaths(int m, int n) {
        int[][] grid = new int[m][n];
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                if (j == 0) grid[0][i] = 1;
                if (i == 0) grid[j][0] = 1;
                if (i != 0 && j != 0) {
                    int left = grid[j][i-1];
                    int up = grid[j-1][i];
                    grid[j][i] = left + up;
                }
            }
        }
        return grid[m-1][n-1];
    }
}
