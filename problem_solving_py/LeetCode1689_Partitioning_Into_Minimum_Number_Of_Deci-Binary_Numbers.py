# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
from typing import List

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minPartitions("82734"))
