from board import Board

board = Board()

while True:
    iniciar_partida = input('Desea iniciar una partida? (S/N): ')
    if iniciar_partida.upper() == 'S':
        board.start()
    else:
        break