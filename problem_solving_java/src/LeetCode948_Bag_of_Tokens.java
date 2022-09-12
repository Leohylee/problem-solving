import java.util.Arrays;

public class LeetCode948_Bag_of_Tokens {

    public static void main(String[] args) {
        LeetCode948_Bag_of_Tokens_Solution solution = new LeetCode948_Bag_of_Tokens_Solution();
        System.out.println(solution.bagOfTokensScore(new int[]{100,200,350,300,400}, 200));
    }

}

class LeetCode948_Bag_of_Tokens_Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        int score = 0;
        int head = 0;
        int tail = tokens.length - 1;
        Arrays.sort(tokens);
        while (head <= tail) {
            if (power >= tokens[head]) {
                power -= tokens[head];
                score++;
                head++;
            } else if (head != tail && score > 0) {
                power += tokens[tail];
                score--;
                tail--;
            } else {
                break;
            }
        }
        return score;
    }
}
