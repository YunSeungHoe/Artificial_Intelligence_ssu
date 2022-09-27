import math
import random
import time

class Tictattoe:
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.maxPlayer = 1 # 'X'
        self.minPlayer = -1 # 'O'

    def main(self):
        print("\n")
        self.show()
        while len(self.empty_idx(self.board)) > 0 and not self.game_over(self.board): # 빈 칸이 있고 게임이 끝나지 않았으면
            self.player_turn(self.board)
            self.com_turn(self.board)
        
        if self.win(self.board, self.maxPlayer):
            print("You win!")
        elif self.win(self.board, self.minPlayer):
            print("You lose...")
        else:
            print("Draw.")

    def evaluate(self, board): # minimax에 사용되는 점수이다.
        # 사람이 이기는 경우는 +1점, 컴퓨터가 이기는 경우는 -1점, 무승부는 0점으로 평가
        if self.win(board, self.maxPlayer): 
            self.score = 1
        elif self.win(board, self.minPlayer):
            self.score = -1
        else:
            self.score = 0
        return self.score
    
    def win(self, board, player): # win 조건에 해당하면 True를 리턴 그렇지 않으면 False를 리턴한다.
        win_cond = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]]

        for c1,c2,c3 in win_cond:
            if board[c1] == board[c2] == board[c3] == player:
                return True
        return False
            
    def player_turn(self, board):
        position = int(input("Your turn : "))
        while position not in self.empty_idx(board):
            print("It exist already.")
            position = int(input("Your turn : "))
            print("\n")
        board[position] = self.maxPlayer
        self.show()
        time.sleep(1)
    
    def com_turn(self, board):
        print("Computer played.")
        depth = len(self.empty_idx(board))
        if depth == 0 or self.game_over(board):
            return
        position, _ = self.minimax(board, depth, self.minPlayer)
        board[position] = self.minPlayer
        self.show()
        time.sleep(1)

    def game_over(self, board): # 게임이 끝났으면 True를 그렇지 않으면 False를 리턴한다.
        return self.win(board, self.maxPlayer) or self.win(board, self.minPlayer)

    def empty_idx(self, board): # 비어 있는 칸의 인덱스를 리스트로 리턴한다.
        empty_list = []
        for i in range(9):
            if board[i] == 0:
                empty_list.append(i)
        return empty_list

    def minimax(self, board, depth, player): # 컴퓨터가 어느 칸에 놓는 것이 최적인지 계산하고 해당 인덱스를 리턴한다.
        # best = [bset_position, best_score]
        if player == self.maxPlayer: # 사람
            best = [-1, -math.inf] 
        elif player == self.minPlayer: # 컴퓨터
            best = [-1, math.inf]

        if depth == 0 or self.game_over(board):
            score = self.evaluate(board)
            return [-1, score]
        
        for idx in self.empty_idx(board):
            board[idx] = player # player가 빈 칸에 돌을 놓는다 가정한다.
            _, score = self.minimax(board, depth-1, -player)
            board[idx] = 0 # 판을 원래대로 돌려 놓는다.

            if player == self.maxPlayer:
                if best[1] < score: # maxPlayer는 max값을 선택한다.
                    best = [idx, score]
            elif player == self.minPlayer:
                if best[1] > score: # minPlayer는 min값을 선택한다.
                    best = [idx, score]
        
        return best
        
    def show(self):
        ox = {-1: 'O', 1: 'X'}
        for i in range(0, 7, 3):
            for j in range(3):
                if j == 2:
                    if self.board[i+j] == 0:
                        print(" ", i+j)
                    else:
                        print(" ", ox[self.board[i+j]])
                else:
                    if self.board[i+j] == 0:
                        print(" ", i+j, "|", end="")
                    else:
                        print(" ", ox[self.board[i+j]], "|", end="")
            print("----|----|----" if i < 7 else "")
        print("\n")


game = Tictattoe()
game.main() 