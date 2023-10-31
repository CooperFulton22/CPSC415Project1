from chess_player import ChessPlayer
import random
from copy import deepcopy

class cfulton_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board, color)

    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        #I am making two dictionaries, one for my moves and one for the opponents moves
        #Each dictionary contains the spot of each piece that can move as a key and each possible spot it can move to as the values
        myMoves = []
        oppMoves = []
        myBoards = []
        oppBoards = []
        FINALMOVE = ()
        finalMoveFound = False

        notationArray = []
        if (self.color == 'white'):
            oppColor = 'black'
            notationArray = ['K', 'Q', 'R', 'B', 'N']
        if (self.color == 'black'):
            oppColor = 'white'
            notationArray = ['k', 'q', 'r', 'b', 'n']

        #First, get all the pieces that can move
        
        for x in self.board.get_all_available_legal_moves(self.color):
            boardNow = deepcopy(self.board)
            originalSpot = x[0]
            print(originalSpot)
            possibleSpotToMove = x[1]
            print(possibleSpotToMove)
            possibleMove = boardNow.make_move(originalSpot, possibleSpotToMove)
            possibleBoard = deepcopy(boardNow)
            tup = (originalSpot, possibleSpotToMove)
            myMoves.append(tup)
            myBoards.append(possibleBoard)
        print("my moves ",  myMoves)
        #print("the first board", myBoards[0])

        for x in self.board.get_all_available_legal_moves(oppColor):
                board = deepcopy(x)
                originalSpot = y[0]
                possibeSpotToMove = y[1]
                possibleMove = board.make_move(originalSpot, possibleSpotToMove)
                possibleBoard = deepcopy(board)
                tup = (originalSpot, possibleSpotToMove)
                oppMoves.append(tup)
                oppBoards.append(possibleBoard)
        
        #if we can make a move to win or get in check we are taking it
        count = 0
        for x in myBoards:
            if x.is_king_in_checkmate(oppColor) == True:
                FINALMOVE = myMoves[count]
                finalMoveFound = True
                break
            count = count + 1
        count = 0
        if finalMoveFound == False:
            for x in myBoards:
                if x.is_king_in_check(oppColor) == True:
                    FINALMOVE = myMoves[count]
                    finalMoveFound = True
                    break
                count = count + 1

        #we are going to see if I'm in check, if so see if I can kill and move there, if not make a random move
        if self.board.is_kind_in_check(self.color) == True:
            count = 0
            for x in myMoves:
                if x[1] = oppMoves[count]:
                    FINALMOVE = x
                    finalMoveFound = True
                    break
                count = count + 1
            if finalMoveFound == False:
                FINALMOVE = random.choice(self.board.get_all_available_legal_moves(self.color))
                finalMoveFound = True

        #next we are going to see if anything is in danger, if so kill the piece threatening if possible if not move out of danger
        for x in oppMoves:
            for y in myMoves: 
                if x[1] == y[0]:
                    #if it gets here opponent can kill me if they wanted


        #if nothing is in danger we are going to eliminate all moves that could result in having a piece taken from me, want to get defensive
        count = 0
        if finalMoveFound == False:
            Possibilities = []
            for x in myBoards:
                if myMoves[count][1] == oppMoves[count][1]:
                    count = count + 1
                else:
                    Possibilities.append(myMoves[count])
                    count = count + 1






        '''for x in self.board.get_all_available_legal_moves(oppColor):
            boardNow = deepcopy(self.board)
            oppOriginalSpot = x[0]
            oppPossibleSpotToMove = x[1]
            possibleMove = boardNow.make_move(oppOriginalSpot, oppPossibleSpotToMove)
            possibleBoard = deepcopy(boardNow)
            if oppOriginalSpot not in oppMovesDict:
                oppMovesDict[oppOriginalSpot] = []
                oppMovesDict[oppOriginalSpot].append(oppPossibleSpotToMove)
                oppBoardsDict[oppOriginalSpot] = []
                oppBoardsDict[oppOriginalSpot].append(possibleBoard)
            else:
                oppMovesDict[oppOriginalSpot].append(oppPossibleSpotToMove)
                oppBoardsDict[oppOriginalSpot].append(possibleBoard)
        print("oppenent moves ", oppMovesDict)
'''
        #next we are going to get rid of all possible moves from my dictionary that can get me killed

        #return FINALMOVE
        return random.choice(self.board.get_all_available_legal_moves(self.color))
