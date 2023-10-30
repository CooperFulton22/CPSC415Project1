from chess_player import ChessPlayer
import random
from copy import deepcopy

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
            boardNow = deepcopy(self.board)
            originalSpot = x[0]
            print(originalSpot)
            possibleSpotToMove = x[1]
            print(possibleSpotToMove)
            possibleMove = boardNow.make_move(originalSpot, possibleSpotToMove)
            possibleBoard = deepcopy(boardNow)
            if originalSpot not in myMovesDict:
                myMovesDict[originalSpot] = []
                myMovesDict[originalSpot].append(possibleBoard)
                print("board added")
            else:
                myMovesDict[originalSpot].append(possibleBoard)
                print("board added again")
        print("my moves ",  myMovesDict)

        for x in self.board.get_all_available_legal_moves(oppColor):
            boardNow = deepcopy(self.board)
            oppOriginalSpot = x[0]
            oppPossibleSpotToMove = x[1]
            possibleMove = boardNow.make_move(oppOriginalSpot, oppPossibleSpotToMove)
            possibleBoard = deepcopy(boardNow)
            if oppOriginalSpot not in oppMovesDict:
                oppMovesDict[oppOriginalSpot] = []
                oppMovesDict[oppOriginalSpot].append(possibleBoard)
            else:
                oppMovesDict[oppOriginalSpot].append(possibleBoard)
        print("oppenent moves ", oppMovesDict)

        #next we are going to get rid of all possible moves from my dictionary that can get me killed


        return random.choice(self.board.get_all_available_legal_moves(self.color))
