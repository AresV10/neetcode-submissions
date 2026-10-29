class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        chars_to_find = list(word)
        pointer = 0
        def findWord(word_chars, curr_location, prev, i, j):
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or (i,j) in prev or board[i][j] != chars_to_find[curr_location]:
                return False
            if curr_location == len(word_chars)-1:
                return True
            
            prev.add((i, j))
            if findWord(chars_to_find, curr_location+1, prev, i-1, j):
                return True
            if findWord(chars_to_find, curr_location+1, prev,i+1, j):
                return True
            if findWord(chars_to_find, curr_location+1, prev,i, j-1):
                return True
            if findWord(chars_to_find, curr_location+1, prev,i, j+1):
                return True
            prev.remove((i,j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == chars_to_find[0]:
                    if findWord(chars_to_find, 0, set(),i, j):
                        return True
        return False
    

