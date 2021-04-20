import game_rules, random
###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

# I will treat these like constants even though they aren't
# Also, these values obviously are not real infinity, but close enough for this purpose
NEG_INF = -1000000000
POS_INF = 1000000000

class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board, symbol):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class has been replaced with the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth): 
        super(MinimaxPlayer, self).__init__(symbol)
        self.limit = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def miniMaxDecision(self, board, depth):
        action = self.maxValue(board, depth)
        print("MOVE: ", action)
        return action[1]

    def maxValue(self, board, depth):
        possibleMoves = game_rules.getLegalMoves(board, self.symbol)
        newMax = NEG_INF
        originalBoard = board
        bestMove = 0

        if self.limit == depth or len(possibleMoves) == 0:
            return [self.h1(board, self.symbol), None]

        for e in possibleMoves:    
            newBoard = game_rules.makeMove(originalBoard, e)
            oldMax = newMax
            compare = self.minValue(newBoard, depth + 1)

            newMax = max(newMax, compare[0])
            if newMax > oldMax:
                oldMax = newMax
                bestMove = e

        pair = [newMax, bestMove]

        if self.symbol == "x":
            self.symbol = "o"
        else:
            self.symbol = "x"

        return pair

    def minValue(self, board, depth):
        possibleMoves = game_rules.getLegalMoves(board, self.symbol)

        newMin = POS_INF
        originalBoard = board
        bestMove = 0

        if self.limit == depth or len(possibleMoves) == 0:
            return [self.h1(board, self.symbol), None]

        for e in possibleMoves:    
            newBoard = game_rules.makeMove(originalBoard, e)
            oldMin = newMin
            compare = self.maxValue(newBoard, depth + 1)

            newMin = min(newMin, compare[0])
            if newMin < oldMin:
                oldMin = newMin
                bestMove = e
            if self.symbol == "x":
                self.symbol = "o"
            else:
                self.symbol = "x"

        pair = [newMin, bestMove]

        return pair
                
    # Edit this one here. :)
    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        
        if len(legalMoves) > 0: 
            depth = -1
            legalMoves[0] = self.miniMaxDecision(board, depth)
            return legalMoves[0]
        else: 
            return None

# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth): 
        self.limit = depth
        super(AlphaBetaPlayer, self).__init__(symbol)

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def abSearch(self, board, depth):
        action = self.maxValue(board, NEG_INF, POS_INF, depth)
        print(action)
        return action[1]

    def maxValue(self, board, alpha, beta, depth):
        possibleMoves = game_rules.getLegalMoves(board, self.symbol)
        maxUtility = alpha
        originalBoard = board
        bestMove = 0

        if self.limit == depth or len(possibleMoves) == 0:
            return [self.h1(board, self.symbol), None]

        for s in possibleMoves:
            newBoard = game_rules.makeMove(originalBoard, s)
            oldUtility = maxUtility
            compare = self.minValue(newBoard, alpha, beta, depth + 1)

            maxUtility = max(maxUtility, compare[0])
            alpha = max(alpha, maxUtility)

            maxUtility = max(maxUtility, compare[0])
            if maxUtility > oldUtility:
                oldUtility = maxUtility
                bestMove = s

            if beta <= alpha:
                return [maxUtility,bestMove]
        if self.symbol == "x":
            self.symbol = "o"
        else:
            self.symbol = "x"

        return [maxUtility, bestMove]

    def minValue(self, board, alpha, beta, depth):
        possibleMoves = game_rules.getLegalMoves(board, self.symbol)
        minUtility = beta
        originalBoard = board
        bestMove = 0

        if self.limit == depth or len(possibleMoves) == 0:
            return [self.h1(board, self.symbol), None]

        for s in board:
            print(s)
            print(originalBoard)
            newBoard = game_rules.makeMove(originalBoard, s)
            oldUtility = minUtility
            compare = self.minValue(newBoard, alpha, beta, depth + 1)

            minUtility = max(minUtility, compare[0])
            beta = max(beta, minUtility)

            if minUtility < oldUtility:
                oldUtility = minUtility
                bestMove = s

            if self.symbol == "x":
                self.symbol = "o"
            else:
                self.symbol = "x"

            if beta <= alpha:
                return [minUtility, bestMove]

        return [minUtility, bestMove]


    # Edit this one here. :)
    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: 
            depth = -1
            legalMoves[0] = self.abSearch(board, depth)
            return legalMoves[0]
        else: 
            return None
            
            
class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None


class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)
