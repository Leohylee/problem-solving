public class LeetCode509_Fibonacci_Number {

    public static void main(String[] args) {
        LeetCode509_Fibonacci_Number_Solution solution = new LeetCode509_Fibonacci_Number_Solution();
        System.out.println(solution.fib(2));
    }

}

class LeetCode509_Fibonacci_Number_Solution {
    public int fib(int n) {
        int res = (n < 2) ? n : fib(n-1) + fib(n-2);
        return res;
    }
}
