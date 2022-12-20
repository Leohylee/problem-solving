// https://leetcode.com/problems/subsets/
//
// Given an integer array nums of unique elements, return all possible subsets (the power set).
//
// The solution set must not contain duplicate subsets. Return the solution in any order.

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode576_Out_of_Boundary_Paths {

    public static void main(String[] args) {
        LeetCode576_Out_of_Boundary_Paths solution = new LeetCode576_Out_of_Boundary_Paths();
        System.out.println(solution.findPaths(8,7,16,1,5));
    }

    private int findPaths(int m, int n, int N, int i, int j) {
        if (N <= 0) return 0;

        final int MOD = 1000000007;
        int[][] count = new int[m][n];
        count[i][j] = 1;
        int result = 0;

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int step = 0; step < N; step++) {
            int[][] temp = new int[m][n];
            for (int r = 0; r < m; r++) {
                for (int c = 0; c < n; c++) {
                    for (int[] d : dirs) {
                        int nr = r + d[0];
                        int nc = c + d[1];
                        if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                            result = (result + count[r][c]) % MOD;
                        }
                        else {
                            temp[nr][nc] = (temp[nr][nc] + count[r][c]) % MOD;
                        }
                    }
                }
            }
            count = temp;
        }

        return result;
    }

}
