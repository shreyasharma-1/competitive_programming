class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c

        def backtrack(r):
            # Base case: All queens placed
            if r == n:
                # Convert board to list of strings
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # If column or diagonals attacked → skip
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place queen
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack: remove queen
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res
