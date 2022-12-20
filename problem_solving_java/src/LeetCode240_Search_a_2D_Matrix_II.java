public class LeetCode240_Search_a_2D_Matrix_II {

    public static void main(String[] args) {
        LeetCode240_Search_a_2D_Matrix_II solution = new LeetCode240_Search_a_2D_Matrix_II();
        System.out.println(solution.searchMatrix(new int[][]{{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}}, 31));
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        int x = 0, y = 0;
        int maxX = matrix[0].length, maxY = matrix.length;
        while (-1 < x && x < maxX && y < maxY) {
            if (matrix[y][x] == target) {
                return true;
            }
            if (x+1 < maxX && matrix[y][x+1] <= target) {
                x++;
                continue;
            }
            if (y+1 < maxY && matrix[y+1][x] <= target) {
                y++;
                continue;
            }
            while (x > 0 && ((y+1 < maxY && matrix[y+1][x] > target) || (y == maxY - 1 && matrix[y][x] != target))) {
                x--;
            }
            if (y < maxY) y++;
        }
        return false;
    }

}
