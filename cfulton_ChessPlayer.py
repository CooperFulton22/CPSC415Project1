from chess_player import ChessPlayer
import random

class cfulton_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board, color)

    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        #I am making two dictionaries, one for my moves and one for the opponents moves
        #Each dictionary contains the spot of each piece that can move as a key and each possible spot it can move to as the values
        myMovesDict = {};
        oppMovesDict = {};
        if (self.color == 'white'):
            oppColor = 'black'
        if (self.color == 'black'):
            oppColor = 'white'

        #First, get all the pieces that can move
        for x in self.board.get_all_available_legal_moves(self.color):
            originalSpot = x[0]
            print(originalSpot)
            possibleSpotToMove = x[1]
            print(possibleSpotToMove)
            if originalSpot not in myMovesDict:
                myMovesDict[originalSpot] = []
                myMovesDict[originalSpot].append(possibleSpotToMove)
            else:
                myMovesDict[originalSpot].append(possibleSpotToMove)
        print("my moves ",  myMovesDict)

        for x in self.board.get_all_available_legal_moves(oppColor):
            oppOriginalSpot = x[0]
            oppPossibleSpotToMove = x[1]
            if oppOriginalSpot not in oppMovesDict:
                oppMovesDict[oppOriginalSpot] = []
                oppMovesDict[oppOriginalSpot].append(oppPossibleSpotToMove)
            else:
                oppMovesDict[oppOriginalSpot].append(oppPossibleSpotToMove)
        print("oppenent moves ", oppMovesDict)

        #next we are going to get rid of all possible moves from my dictionary that can get me killed
        for x in myMovesDict:
            #print("x is ", x)
            for y in myMovesDict[x]:
                #print("y is ", y)
                for z in oppMovesDict:
                    #print("z is ", z)
                    for w in oppMovesDict[z]:
                        #print("w is ", w)
                        if y == w:
                            #print("time for removal")
                            myMovesDict[x].remove(y)
        print("my moves ", myMovesDict)
        #print(self.board.get_all_available_legal_moves(self.color))

        return random.choice(self.board.get_all_available_legal_moves(self.color))
