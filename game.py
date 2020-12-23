import board
import moves
import chess_ai

def main():
    board.printboard()
    while True:
        moves.make_move()
        moves.halfmove_checker += 1

        #Checks for threefold repition
        if moves.threefold_check():
            print("\nDraw by threefold repition")
            break
        
        #Checks for 50 move rule
        if moves.halfmove_checker == 99:
            print("\nDraw by 50 move rule")
            break

main()