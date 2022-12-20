// https://leetcode.com/problems/word-pattern/
//
// Given a pattern and a string s, find if s follows the same pattern.
//
// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

import java.util.ArrayList;
import java.util.List;

public class LeetCode290_Word_Pattern {

    public static void main(String[] args) {
        LeetCode290_Word_Pattern solution = new LeetCode290_Word_Pattern();
        System.out.println(solution.wordPattern("abba", "dog cat cat dog"));
    }

    private boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (words.length != pattern.length()) return false;
        List<Character> chars = new ArrayList();
        int[] sequence = new int[pattern.length()];
        int index = 0;
        for (char str : pattern.toCharArray()) {
            if (!chars.contains(str)) {
                chars.add(str);
            }
            sequence[index] = chars.indexOf(str);
            index++;
        }
        List<String> listOfWords = new ArrayList<>();
        boolean samePattern;
        index = 0;
        for (String word : words) {
            if (!listOfWords.contains(word)) {
                listOfWords.add(word);
            }
            samePattern = (listOfWords.indexOf(word) == sequence[index]);
            if (!samePattern) return false;
            index++;
        }
        return true;
    }

}