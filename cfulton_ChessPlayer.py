from chess_player import ChessPlayer
import random
from copy import deepcopy
import builtins
import chess_config
from chess_model import Board

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
        print("alright here we go\n") 
        for x in self.board.get_all_available_legal_moves(self.color):
            boardNow = deepcopy(self.board)
            originalSpot = x[0]
            #print(originalSpot)
            possibleSpotToMove = x[1]
            #print(possibleSpotToMove)
            possibleMove = boardNow.make_move(originalSpot, possibleSpotToMove)
            possibleBoard = deepcopy(boardNow)
            tup = (originalSpot, possibleSpotToMove)
            myMoves.append(tup)
            myBoards.append(possibleBoard)
        print("got my moves\n")
        print("my moves", myMoves)
        #print("the first board", myBoards[0])

        for x in self.board.get_all_available_legal_moves(oppColor):
            boardNow2 = deepcopy(self.board)
            #print("board copied and heres the move", x)
            originalSpot2 = x[0]
            possibleSpotToMove2 = x[1]
            possibleMove2 = boardNow2.make_move(originalSpot2, possibleSpotToMove2)
            #print("got the move")
            possibleBoard2 = deepcopy(boardNow2)
            #print("board copied")
            tup2 = (originalSpot2, possibleSpotToMove2)
            oppMoves.append(tup2)
            #print("tup added")
            oppBoards.append(possibleBoard2)
            #print("board added")
        print("got the opponent moves\n")
        print("opp moves", oppMoves)
        #if we can make a move to win or get in check we are taking it
        if finalMoveFound == False:
            count = 0
            for x in myBoards:
                if x.is_king_in_checkmate(oppColor) == True:
                    FINALMOVE = myMoves[count]
                    print("checkmate move")
                    finalMoveFound = True
                    break
                count = count + 1
            count = 0
            print("ok so can't win here\n")
        if finalMoveFound == False:            
            for x in myBoards:
                if x.is_king_in_check(oppColor) == True:
                    FINALMOVE = myMoves[count]
                    print("check move")
                    finalMoveFound = True
                    break
                count = count + 1
            
        if finalMoveFound == False:
        #we are going to see if I'm in check, if so see if I can kill and move there, if not make a random move
            if self.board.is_king_in_check(self.color) == True:
                count = 0
                for x in myMoves:
                    if x[1] == oppMoves[count]:
                        FINALMOVE = x
                        print("killed out of check")
                        finalMoveFound = True
                        break
                    count = count + 1
                FINALMOVE = random.choice(self.board.get_all_available_legal_moves(self.color))
                print("moved out of check")
                finalMoveFound = True
            print("not in check\n")
        if finalMoveFound == False:
        #next we are going to see if anything is in danger, if so kill the piece threatening if possible if not move out of danger
            spotToTryToKill = ""
            spotInDanger = ""
            spotFound = False
            Possibilities = []
            for x in myMoves:
                for y in oppMoves: 
                    if y[1] == x[0]:
                        #if it gets here opponent can kill me if they wanted
                        spotToTryToKill = y[0]
                        spotInDanger = x[0]
                        spotFound = True
                        print("danger found")
                        break
            if spotFound == True:
                for x in myMoves:
                    if x[1] == spotToTryToKill:
                        FINALMOVE = x
                        print("kill out of danger")
                        finalMoveFound = True
                        break
        #if finalMoveFound == False:
            if spotFound == False:
                for x in myMoves:
                    if x[0] == spotInDanger:
                        Possibilities.append(x)
                        #now we have the possible moves to move the dangered piece
                for x in oppMoves:
                    for y in Possibilities:
                        if x[1] == y[1]:
                            Possibilities.remove(y)
                if Possibilities == []:
                    for x in myMoves:
                        if x[0] == spotInDanger:
                            FINALMOVE = x
                            print("moved from danger but still in danger")
                            finalMoveFound = True
                            break
                else:
                    FINALMOVE = random.choice(Possibilities)
                    print("moved from danger to safety")
                    finalMoveFound = True
                    

        if finalMoveFound == False:
            #if nothing is in danger we are going to eliminate all moves that could result in having a piece taken from me, want to get defensive
            count = 0
            for x in myMoves:
                for y in oppMoves:
                    if x[1] != y[1]:
                        Possibilities.append(x)
            
            #just returning a random safe move temporarily
            FINALMOVE = random.choice(Possibilities)
            print("random safe move")
            finalMoveFound = True
            
        if finalMoveFound == False:

            #just in case my code sucks returning random move
            FINALMOVE = random.choice(self.board.get_all_available_legal_moves(self.color))
            print("completely random move")
            finalMoveFound = True
            


        
        return FINALMOVE
        
