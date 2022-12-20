// https://leetcode.com/problems/koko-eating-bananas/
//
// TKoko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
// and will come back in h hours.
//
// Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
// bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
// more bananas during this hour.
//
// Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
//
// Return the minimum integer k such that she can eat all the bananas within h hours.
//

public class LeetCode875_Koko_Eating_Bananas {

    public static void main(String[] args) {
        LeetCode875_Koko_Eating_Bananas solution = new LeetCode875_Koko_Eating_Bananas();
        System.out.println(solution.minEatingSpeed(new int[]{3,6,7,11}, 8));
    }

    private int minEatingSpeed(int[] piles, int h) {
        int max = 1;
        int min = 1;
        for (int num : piles) {
            if (num > max) {
                max = num;
            }
        }
        int ans = 1;
        int mid = 1;
        while (min <= max) {
            mid = (max + min) / 2;
            if (canEatInTime(mid, piles, h)) {
                ans = mid;
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }
        return ans;
    }

    private boolean canEatInTime(int mid, int[] piles, int time) {
        int sum = 0;
        for (int bananas : piles) {
            sum += (Math.ceil((double) bananas / (double) mid) <= 1) ? 1 : Math.ceil((double) bananas / (double) mid);
            if (sum > time) return false;
        }
        return true;
    }

}
