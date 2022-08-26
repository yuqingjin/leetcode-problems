# Method: hash set
# T: O(n^2)
# S: O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != ".":
                    box_num = (i//3) * 3 + j // 3
                    # if cur in rows[i]:
                    #     return False
                    # if cur in cols[j]:
                    #     return False
                    # if cur in boxes[box_num]:
                    #     return False
                    
                    if cur in rows[i] or cur in cols[j] or cur in boxes[box_num]:
                        return False
                    
                    # 这么写不行
#                     if cur in (rows[i] or cols[j] or boxes[box_num]):
#                         return False
                    
                    rows[i].add(cur)
                    cols[j].add(cur)
                    boxes[box_num].add(cur)
        return True
