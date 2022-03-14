# https://leetcode.com/problems/simplify-path/


class Solution(object):
    def simplifyPath(self, path):
        paths = []
        folder = ""
        for i in range(0, len(path)):
            if path[i] != "/":
                folder = folder + path[i]
            if path[i] == "/" or i + 1 >= len(path):
                match folder:
                    case "":
                        pass
                    case "..":
                        if len(paths) > 0:
                            paths.pop(-1)
                    case ".":
                        pass
                    case _:
                        paths.append(folder)
                folder = ""
        return "/" + "/".join(paths)


if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/../"))
