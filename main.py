import chess
from Constants import valueTable 
from randomBoard import stockfish, random_board


board = chess.Board()
print(stockfish(random_board(), 200))



def isGameEnded():
    if board.is_checkmate():
            if board.turn:
                return -9999
            else:
                return 9999
    if board.is_stalemate():
            return 0
    if board.is_insufficient_material():
            return 0
    
def getWhiteScore():
    whitePawn = len(board.pieces(chess.PAWN, chess.WHITE))
    blackPawn = len(board.pieces(chess.PAWN, chess.BLACK))
    WhiteKnight = len(board.pieces(chess.KNIGHT, chess.WHITE))
    BlackKnight = len(board.pieces(chess.KNIGHT, chess.BLACK))
    WhiteBishop = len(board.pieces(chess.BISHOP, chess.WHITE))
    BlackBishop = len(board.pieces(chess.BISHOP, chess.BLACK))
    WhiteRook = len(board.pieces(chess.ROOK, chess.WHITE))
    BlackRook = len(board.pieces(chess.ROOK, chess.BLACK))
    WhiteQueen = len(board.pieces(chess.QUEEN, chess.WHITE))
    BlackQueen = len(board.pieces(chess.QUEEN, chess.BLACK))


    material = 100 * (whitePawn - blackPawn) + 320 * (WhiteKnight - BlackKnight) + 330 * (WhiteBishop - BlackBishop) + 500 * (WhiteRook - BlackRook) + 900 * (WhiteQueen - BlackQueen)
    
    pawnsq = sum([valueTable.pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])

    pawnsq = pawnsq + sum([-valueTable.pawntable[chess.square_mirror(i)] for i in board.pieces(chess.PAWN, chess.BLACK)])
    
    knightsq = sum([valueTable.knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-valueTable.knightstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    
    bishopsq = sum([valueTable.bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq = bishopsq + sum([-valueTable.bishopstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.BISHOP, chess.BLACK)])
    
    rooksq = sum([valueTable.rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
    rooksq = rooksq + sum([-valueTable.rookstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.ROOK, chess.BLACK)])
    
    queensq = sum([valueTable.queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
    queensq = queensq + sum([-valueTable.queenstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.QUEEN, chess.BLACK)])
    
    kingsq = sum([valueTable.kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
    kingsq = kingsq + sum([-valueTable.kingstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.KING, chess.BLACK)])
    
    eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if board.turn:
        return eval
    else:
        return -eval