# https://leetcode.com/problems/game-of-life/

from collections import defaultdict
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if len(board) > 0:
            cells_cnt = [[0] * len(board[0]) for _ in range(len(board))]
            for row_idx, row in enumerate(board):
                for idx, num in enumerate(row):
                    if len(board) == 1:
                        cells_cnt[row_idx][idx] = sum([sum(board[row_idx][idx - 1 if idx - 1 >= 0 else 0:idx + 2])])
                    elif row_idx == 0:
                        cells_cnt[row_idx][idx] = sum([sum(board[row_idx][idx-1 if idx-1 >= 0 else 0:idx+2]), sum(board[row_idx+1][idx-1 if idx-1 >= 0 else 0:idx+2])])
                    elif 0 < row_idx < len(board) - 1:
                        cells_cnt[row_idx][idx] = sum([sum(board[row_idx-1][idx-1 if idx-1 >= 0 else 0:idx+2]), sum(board[row_idx][idx-1 if idx-1 >= 0 else 0:idx+2]), sum(board[row_idx+1][idx-1 if idx-1 >= 0 else 0:idx+2])])
                    else:
                        cells_cnt[row_idx][idx] = sum([sum(board[row_idx-1][idx - 1 if idx - 1 >= 0 else 0:idx + 2]), sum(board[row_idx][idx - 1 if idx - 1 >= 0 else 0:idx + 2])])
            for row_idx, row in enumerate(board):
                for idx, num in enumerate(row):
                    neighbors = cells_cnt[row_idx][idx] - num
                    if num == 1:
                        if neighbors < 2 or neighbors > 3:
                            board[row_idx][idx] = 0
                    elif num == 0:
                        if neighbors == 3:
                            board[row_idx][idx] = 1
            return board



if __name__ == "__main__":
    solution = Solution()
    print(solution.gameOfLife([[0]]))
