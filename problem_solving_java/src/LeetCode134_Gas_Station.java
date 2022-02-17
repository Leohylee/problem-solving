// https://leetcode.com/problems/gas-station/
//
// There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
//
// You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its
// next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
//
// Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the
// circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be
// unique

public class LeetCode134_Gas_Station {

    public static void main(String[] args) {
        LeetCode134_Gas_Station_Solution solution = new LeetCode134_Gas_Station_Solution();
        System.out.println(solution.canCompleteCircuit(new int[]{1,2,3,4,5}, new int[]{3,4,5,1,2}));
    }

}

class LeetCode134_Gas_Station_Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int sum = 0, n = gas.length;
        int gasInTank = 0, start = 0;
        for(int i=0;i<n;i++) {
            gasInTank += gas[i]-cost[i];
            sum += gas[i]-cost[i];
            // if we are not able to reach next station from i,
            if(gasInTank < 0) {
                start = i+1;
                gasInTank = 0;
            }
        }

        return sum >= 0 ? start : -1;
    }
}
