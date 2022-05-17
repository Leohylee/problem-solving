# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        value = target.val
        queue = [cloned]
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr:
                if curr.val == value:
                    return curr
                queue.append(curr.left)
                queue.append(curr.right)
        return -1


if __name__ == "__main__":
    solution = Solution()
    target = TreeNode(3, TreeNode(6), TreeNode(19))
    original = TreeNode(7, TreeNode(4), target)
    cloned = TreeNode(7, TreeNode(4, TreeNode(None)), TreeNode(3, TreeNode(6), TreeNode(19)))
    print(solution.getTargetCopy(original, cloned, target))
