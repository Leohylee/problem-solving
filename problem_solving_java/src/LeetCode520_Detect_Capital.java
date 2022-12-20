// https://leetcode.com/problems/detect-capital/
//
// We define the usage of capitals in a word to be right when one of the following cases holds:
//
// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".

public class LeetCode520_Detect_Capital {

    public static void main(String[] args) {
        LeetCode520_Detect_Capital solution = new LeetCode520_Detect_Capital();
        System.out.println(solution.detectCapitalUse("USA"));
    }

    private boolean detectCapitalUse(String word) {
        if (word.length() < 2) return true;
        boolean firstLowerCase = Character.isLowerCase(word.charAt(0));
        boolean secondLowerCase = Character.isLowerCase(word.charAt(1));
        String remain = word.substring(1);
        for (char ch : remain.toCharArray()) {
            boolean currentLowerCase = Character.isLowerCase(ch);
            if ((firstLowerCase && !currentLowerCase) || (secondLowerCase != currentLowerCase)) return false;
        }
        return true;
    }

}
