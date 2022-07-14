public class LeetCode473_Matchsticks_to_Square {
    public static void main(String[] args) {
        LeetCode473_Matchsticks_to_Square_Solution solution = new LeetCode473_Matchsticks_to_Square_Solution();
        System.out.println(solution.makesquare(new int[]{1,1,3,3,3,1}));
    }
}

class LeetCode473_Matchsticks_to_Square_Solution {
    public int[] square = new int[4];
    public int[] matchsticks;
    public int sideLength;

    public boolean makesquare(int[] matchsticks) {
        if (matchsticks.length < 4) return false;
        int sum = 0;
        for (int matchstick : matchsticks) {
            sum += matchstick;
        }
        sideLength = sum / 4;
        if (sideLength * 4 != sum) {
            return false;
        }
        this.matchsticks = matchsticks;
        return dfs(matchsticks.length - 1);
    }

    public boolean dfs(int currentStick) {
        if (currentStick < 0) return square[0] == square[1] && square[1] == square[2] && square[2] == square[3];
        for (int i = 0; i < 4; i++) {
            if (matchsticks[currentStick] <= sideLength - square[i]){
                square[i] += matchsticks[currentStick];
                if (dfs(currentStick - 1)) {
                    return true;
                }
                square[i] -= matchsticks[currentStick];
            }
        }
        return false;
    }
}