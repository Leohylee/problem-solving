# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        length = max(len(version1), len(version2))
        for i in range(0, length):
            if i < len(version1) and i < len(version2):
                if int(version1[i]) > int(version2[i]):
                    return 1
                elif int(version1[i]) < int(version2[i]):
                    return -1
            else:
                if i < len(version1) and int(version1[i]) > 0:
                    return 1
                elif i < len(version2) and int(version2[i]) > 0:
                    return -1
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.compareVersion("1.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0", "1.0.0.1"))
