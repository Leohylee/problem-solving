public class LeetCode242_Valid_Anagram {

    public static void main(String[] args) {
        LeetCode242_Valid_Anagram_Solution solution = new LeetCode242_Valid_Anagram_Solution();
        System.out.println(solution.isAnagram("rat", "car"));
    }

}

class LeetCode242_Valid_Anagram_Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i)-'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i)-'a']--;
        for (int i = 0; i < alphabet.length; i++) if (alphabet[i] != 0) return false;
        return true;
    }
}
