# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length

        # n = len(s)
        # if n < 2: return n
        # ans, head, tail = 1, 0, 0
        # dic = {s[0]: 1}
        # while head < n - 1 and tail < n:
        #     if all(val < 2 for val in dic.values()):
        #         ans = len(dic) if len(dic) > ans else ans
        #         tail += 1
        #         if tail < n:
        #             if s[tail] not in dic:
        #                 dic[s[tail]] = 1
        #             else:
        #                 dic[s[tail]] += 1
        #     else:
        #         dic[s[head]] -= 1
        #         if dic[s[head]] == 0: dic.pop(s[head])
        #         head += 1
        # return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("afgdfgau"))
