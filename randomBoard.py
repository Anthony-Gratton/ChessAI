import chess
import chess.engine
import random
import numpy
from stockfish import Stockfish


def random_board(max_depth=200):
    board = chess.Board()
    depth = random.randrange(0, max_depth)

    for _ in range(depth):
        all_moves = list(board.legal_moves)
        random_move = random.choice(all_moves)
        board.push(random_move)
        if board.is_game_over():
            board.pop()
            break

    return board


# this function will create our f(x) (score)
def stockfish(board: chess.Board):
    boardfen = board.board_fen()
    stockfishinstance = Stockfish(path="D:/2060246/ChessAI/stockfish-windows-x86-64-avx2/stockfish/stockfish.exe")
    stockfishinstance.set_fen_position(boardfen)
    try:
        boardev = stockfishinstance.get_evaluation()
        boardev["board"] = board
        del stockfishinstance
        return boardev
    except:
        del stockfishinstance
        return {'type': 'none', 'value': 0, 'board': ''}
