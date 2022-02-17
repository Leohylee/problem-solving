// https://leetcode.com/problems/can-place-flowers/
//
// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be
// planted in adjacent plots.
//
// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an
// integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

public class LeetCode605_Can_Place_Flowers {

    public static void main(String[] args) {
        LeetCode605_Can_Place_Flowers_Solution solution = new LeetCode605_Can_Place_Flowers_Solution();
        System.out.println(solution.canPlaceFlowers(new int[]{1,0,0,0,1}, 1));
    }

}

class LeetCode605_Can_Place_Flowers_Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int prev = 0;
        int next = 0;
        for (int slot = 0; slot < flowerbed.length; slot++) {
            next = (next + 1 < flowerbed.length) ? next + 1 : next;
            prev = (slot - 1 > 0) ? slot - 1 : 0;
            if (flowerbed[slot] == 1) continue;
            if (flowerbed[prev] == 0 && flowerbed[next] == 0) {
                flowerbed[slot] = 1;
                count++;
            }
        };
        return count >= n;
    }
}
