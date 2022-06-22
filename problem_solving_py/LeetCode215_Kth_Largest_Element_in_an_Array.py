# https://leetcode.com/problems/kth-largest-element-in-an-array/
import random


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums)[-k]

    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]



if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
