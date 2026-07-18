class Solution:
    def by3isValid(self,part:List[List[str]])-> bool:
        checker = set()
        for i in part:
            for j in i:
                if j == ".":
                    continue
                elif j in checker:
                    return False
                else:
                    checker.add(j)
        return True
    def rcIsValid(self,row:List[str])->bool:
        checker=set()
        for i in row:
            if i ==".":
                continue
            elif i in checker:
                return False
            else:
                checker.add(i)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if not self.rcIsValid(i):
                return False
        for j in range(9):
            column = []
            for i in board:
                column.append(i[j])
            if not self.rcIsValid(column):
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                part = []

                for row in range(box_row, box_row + 3):
                    part.append(
                        board[row][box_col:box_col + 3]
                    )

                if not self.by3isValid(part):
                    return False

        return True

        


        