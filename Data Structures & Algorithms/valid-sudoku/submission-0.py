class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d == ".":
                    continue
                if d in rows[i] or d in columns[j] or d in boxs[(i//3, j//3)]:
                    return False
                rows[i].add(d)
                columns[j].add(d)
                boxs[(i//3, j//3)].add(d)

        return True