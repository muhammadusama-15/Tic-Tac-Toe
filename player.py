class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = None

    def put_mark(self,game,coordinates):
        row = int(coordinates.split(",")[0])
        column = int(coordinates.split(",")[1])

        try:
            if game[row-1][column-1] == "_":
                game[row-1][column-1] = game[row-1][column-1].replace("_",self.symbol)
                self.marked = True

            elif game[row-1][column-1] != "_":
                print(f"The cell is occupied. {self.name} try again: ")
                self.marked = False
        except IndexError:
            print(f"The cell does not exist. {self.name} try again: ")
            self.marked = False

    def is_winner(self,game):
        winner = False
        #Checking if criss-cross line is formed.
        if game[0][0]==game[1][1]==game[2][2]==self.symbol or game[0][2]==game[1][1]==game[2][0]==self.symbol:
            winner = True
            return winner
        
        #Checking if a row or column is same.
        else:
            for i in range(len(game)):
                if game[0][i]==game[1][i]==game[2][i]==self.symbol or game[i][0]==game[i][1]==game[i][2]==self.symbol:
                    winner = True
            return winner
        