# https://leetcode.com/problems/smallest-string-with-swaps/
from collections import defaultdict
from typing import List


class Solution:
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 1. Union-Find
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)

        # 2. Grouping
        group = defaultdict(lambda: ([], []))
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

        # 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch

        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestStringWithSwaps("nhrqzrqhxvblouv", [[8,6],[7,4],[1,8],[9,5],[13,2],[11,12],[7,1],[2,13],[13,7],[12,5],[13,13],[2,11],[14,12],[6,11],[6,3]]))
