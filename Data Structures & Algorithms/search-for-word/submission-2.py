class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars_to_find = list(word)
        pointer = 0
        def findWord(word_chars, curr_location, prev, i, j):
            if curr_location == len(word_chars)-1:
                if board[i][j] == chars_to_find[curr_location]:
                    return True
                else:
                    return False
            present = False
            if i > 0 and (i-1, j) not in prev and board[i-1][j] == chars_to_find[curr_location+1]:
                temp = prev.copy()
                temp.add((i-1, j))
                present = present or findWord(chars_to_find, curr_location+1, temp, i-1, j)
            if i < len(board)-1 and (i+1, j) not in prev and board[i+1][j] == chars_to_find[curr_location+1]:
                temp = prev.copy()
                temp.add((i+1, j)) 
                present = present or findWord(chars_to_find, curr_location+1, temp,i+1, j)
            if j > 0 and (i, j-1) not in prev and board[i][j-1] == chars_to_find[curr_location+1]:
                temp = prev.copy()
                temp.add((i, j-1))
                present = present or findWord(chars_to_find, curr_location+1, temp,i, j-1)
            if j < len(board[0])-1 and (i, j+1) not in prev and board[i][j+1] == chars_to_find[curr_location+1]:
                temp = prev.copy()
                temp.add((i, j+1))
                present = present or findWord(chars_to_find, curr_location+1, temp,i, j+1)
            return present

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == chars_to_find[0]:
                    if findWord(chars_to_find, 0, {(i,j)},i, j):
                        return True
        return False
    

