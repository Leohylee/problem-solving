public class LeetCode509_Fibonacci_Number {

    public static void main(String[] args) {
        LeetCode509_Fibonacci_Number solution = new LeetCode509_Fibonacci_Number();
        System.out.println(solution.fib(2));
    }

    private int fib(int n) {
        return (n < 2) ? n : fib(n-1) + fib(n-2);
    }

}
