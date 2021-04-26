# https://leetcode.com/problems/word-search-ii/
from typing import List

class Solution(object):
    def searching(self, board, row, col, words, finallist, tempstr):
        holderchar = board[row][col]
        board[row][col] = 0
        tempstr = tempstr + holderchar

        if tempstr in words:
            words.remove(tempstr)
            finallist.append(tempstr)

        if row - 1 >= 0 and board[row - 1][col] != 0 and len(tempstr) < self.wordlength:
            self.searching(board, row - 1, col, words, finallist, tempstr)

        if row + 1 < len(board) and board[row + 1][col] != 0 and len(tempstr) < self.wordlength:
            self.searching(board, row + 1, col, words, finallist, tempstr)

        if col - 1 >= 0 and board[row][col - 1] != 0 and len(tempstr) < self.wordlength:
            self.searching(board, row, col - 1, words, finallist, tempstr)

        if col + 1 < len(board[0]) and board[row][col + 1] != 0 and len(tempstr) < self.wordlength:
            self.searching(board, row, col + 1, words, finallist, tempstr)

        board[row][col] = holderchar


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row = len(board)
        col = len(board[0])
        finallist = []

        self.wordlength = len(max(words, key=len))

        for x in range(row):
            for y in range(col):
                tempstr = ""
                self.searching(board, x, y, words, finallist, tempstr)

        return finallist


res = Solution().findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],["i", "f", "l", "v"]], words=["oath", "pea", "eat", "rain"])
print(res)