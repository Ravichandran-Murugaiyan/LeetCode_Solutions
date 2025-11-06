class Solution:
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()       # columns with queens
        posDiag = set()    # (r + c) diagonals
        negDiag = set()    # (r - c) diagonals

        def backtrack(r):
            if r == n:
                # convert board to list of strings
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                # remove queen (backtrack)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res
