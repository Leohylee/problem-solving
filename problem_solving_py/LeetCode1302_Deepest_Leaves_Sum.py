# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        pairs, stack = [], [(level, root)]
        while len(stack) > 0:
            lv, curr = stack.pop(0)
            if curr is not None:
                pairs.append((lv, curr.val))
                level = lv + 1
                stack.append((level, curr.left))
                stack.append((level, curr.right))
        sum = 0
        for lv, val in pairs:
            if lv == level - 1:
                sum += val
        return sum


if __name__ == "__main__":
    solution = Solution()
    treeNode = TreeNode(1)
    print(solution.deepestLeavesSum(treeNode))
