# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return
        root.next = 0
        stack, order = [root], []
        while len(stack) > 0:
            curr = stack.pop(0)
            order.append(curr)
            if curr.left is not None:
                curr.left.next = curr.next + 1
                stack.append(curr.left)
            if curr.right is not None:
                curr.right.next = curr.next + 1
                stack.append(curr.right)
        for i in range(len(order)):
            if i + 1 < len(order) and order[i].next == order[i+1].next:
                order[i].next = order[i+1]
            else:
                order[i].next = None
        return root



if __name__ == "__main__":
    solution = Solution()
    node = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    print(solution.connect(None))
