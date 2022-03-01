# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root):
        maxLen = left = 1
        currLevel = 0
        queue = [(0, 1, root)]
        for level, pos, node in queue:
            if node is not None:
                if currLevel != level:
                    left = pos
                    currLevel = level
                maxLen = max(pos - left + 1, maxLen)
                queue.append((level + 1, pos * 2, node.left))
                queue.append((level + 1, pos * 2 + 1, node.right))
        return maxLen


if __name__ == "__main__":
    solution = Solution()
    node = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6)), None), TreeNode(2, None, TreeNode(9, None, TreeNode(7))))
    print(solution.widthOfBinaryTree(node))
