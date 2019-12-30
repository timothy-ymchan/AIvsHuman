class Player:
    def __init__(self, name):
        self.name = name
    def move(self, info={}):
        board = 0
        cell = 0
        valid = True
        command = input("Player {}: ".format(self.name))
        if len(command) > 2:
            valid = False
        else:
            if ord(command[0]) >= ord('A') and ord(command[0]) <= ord('C'):
                board = ord(command[0]) - ord('A')
            else:
                valid = False
            if ord(command[1]) >= ord('0') and ord(command[1]) <= ord('8'):
                cell = int(command[1])
            else:
                valid = False
        return board,cell,valid
