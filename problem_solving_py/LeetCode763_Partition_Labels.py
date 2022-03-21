# https://leetcode.com/problems/partition-labels/

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0: return []
        ans = []
        head = {}
        tail = {}
        for i in range(0, len(s)):
            if head.get(s[i]) is None:
                head[s[i]] = i
                tail[s[i]] = i
            else:
                tail[s[i]] = i
        sort_key = sorted(head, key=head.get)
        first = last = None
        for key in sort_key:
            if first is None and last is None:
                first = head.get(key)
                last = tail.get(key)
            elif head.get(key) < last < tail.get(key):
                last = tail.get(key)
            elif head.get(key) > last:
                ans.append(last - first + 1)
                first = head.get(key)
                last = tail.get(key)
        ans.append(last - first + 1)
        return ans



if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels(""))
