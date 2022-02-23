# https://leetcode.com/problems/subsets/
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        hm = {node: Node(node.val)}
        self.addNeighbors(node, hm)
        return hm[node]

    def addNeighbors(self, node: 'Node', hm):
        for neighbor in node.neighbors:
            if neighbor not in hm:
                hm[neighbor] = Node(neighbor.val)
                self.addNeighbors(neighbor, hm)
            hm[node].neighbors.append(hm[neighbor])

    # def cloneGraph(self, node):  # DFS recursively
    #     if not node:
    #         return node
    #     m = {node: Node(node.val)}
    #     self.dfs(node, m)
    #     return m[node]
    #
    # def dfs(self, node, m):
    #     for neigh in node.neighbors:
    #         if neigh not in m:
    #             m[neigh] = Node(neigh.val)
    #             self.dfs(neigh, m)
    #         m[node].neighbors.append(m[neigh])


if __name__ == "__main__":
    solution = Solution()
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print(solution.cloneGraph(node1))
