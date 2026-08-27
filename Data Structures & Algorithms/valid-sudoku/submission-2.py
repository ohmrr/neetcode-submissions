class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # Key : Val => Row # : set(...)
        cols = defaultdict(set) # Key : Val => Col # : set(...)
        squares = defaultdict(set) # Key : Val => (Row // 3, Col // 3) : set(...)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rows[r]:
                    return False
                elif board[r][c] in cols[c]:
                    return False
                elif board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True