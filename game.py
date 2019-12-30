import player
class Game:
    def __init__(self):
        self.board = [[x for x in range(0,9)] for y in range(0,3)]
        self.kill = [False for x in range(0,3)]
    def setBoard(self, board, cell):
        if not self.kill[board] and self.board[board][cell] != 'X':
            self.board[board][cell] = 'X'
            return True
        else:
            return False
    def checkKill(self,board):
        if self.kill[board] == True:
            return True
        else:
            isKill = False
            #Check vertical
            for i in range(0,3):
                if self.board[board][i] == 'X' and self.board[board][3+i] == 'X' and self.board[board][6+i] == 'X':
                    isKill = True
            #Check horizontal
            for i in range(0,3):
                if self.board[board][i*3] == 'X' and self.board[board][i*3+1] == 'X' and self.board[board][i*3+2] == 'X':
                    isKill = True
            #Check diagonal
            if self.board[board][0] == 'X' and self.board[board][4] == 'X' and self.board[board][8] == 'X':
                isKill = True
            if self.board[board][2] == 'X' and self.board[board][4] == 'X' and self.board[board][6] == 'X':
                isKill = True

            return isKill

    def display(self):
        for board in range(0,3):
            if not self.kill[board]:
                print("{:7}".format(chr(65+board)),end="")
        print("")
        for row in range(0,3):
            for board in range(0,3):
                if not self.kill[board]:
                    for col in range(0,3):
                        print("{} ".format(self.board[board][row*3+col]),end="")
                    print(" ",end="")
            print("")

    def main(self):
        #Main loop
        gameover = False
        currentPlayer = 0
        players = [player.Player("1"), player.Player("2")]
        while not gameover:
            #Display current configuration
            self.display()

            #Allow current player to move
            board, move, validInput = players[currentPlayer].move()

            if validInput:
                validMove = self.setBoard(board,move)
                if validMove:
                    #Update player
                    currentPlayer = (currentPlayer + 1) %2

            #Prompt Error Message
            if not validInput or not validMove:
                print("Invalid input")

            #Do game over checking
            allKill = True
            for _board in range(0,3):
                if self.checkKill(_board) == True:
                    self.kill[_board] = True
                else:
                    allKill = False
            if allKill:
                gameover = True
        print("Player {} wins game".format(currentPlayer +1))



if __name__ == '__main__':
    game = Game()
    game.main()