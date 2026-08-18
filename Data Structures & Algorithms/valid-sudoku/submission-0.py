class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        boxs=set()

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num=board[r][c]
                if(r,num) in row:
                    return False
                if(c,num) in col:
                    return False
                box=(r//3,c//3)
                if(box,num) in boxs:
                    return False

                row.add((r,num))
                col.add((c,num))
                boxs.add((box,num))

        return True

        