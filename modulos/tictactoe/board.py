from player import Player

class Board:
    def __init__(self):
        self.board_status = {   'c1': '', 'c2': '', 'c3': '',
                                'c4': '', 'c5': '', 'c6': '',
                                'c7': '', 'c8': '', 'c9': '',
                            }

        self.winning_conditions = ( ('c1', 'c2', 'c3'), ('c4', 'c5', 'c6'), ('c7', 'c8', 'c9'),
                                    ('c1', 'c4', 'c7'), ('c2', 'c5', 'c8'), ('c3', 'c6', 'c9'),
                                    ('c1', 'c5', 'c9'), ('c3', 'c5', 'c7'))

        self.player_1 = Player('X')
        self.player_2 = Player('O')

        self.current_player = self.player_1


    def render_instructions(self):
        # Mostrar las instrucciones del juego

        print(' -  TIC TAC TOE  - ')
        print('\n')
        print('  c1  |  c2  |  c3  \n------+------+------\n  c4  |  c5  |  c6  \n------+------+------\n  c7  |  c8  |  c9  ')
        print('\n')
        print('Jugador 1: X - Jugador 2: O')
        print('En cada turno el jugador deberá insertar la celda que va utilizar.')


    def render_board_status(self):
        # Motrar el tablero con los valores de cada celda

        print('   {}   |   {}   |   {}   \n------+------+------\n   {}   |   {}   |   {}   \n------+------+------\n   {}   |   {}   |   {}   '.format(*self.board_status.values()))

    
    def check_board(self):
        # Verificar el tablero para determinar si existe un ganador
        # Retorna: 'G' (si existe un ganador), 'E' (si es empate) o 'C' (si el juego continua)
        
        exists_winner = False;

        for winning_condition in self.winning_conditions:
            a = self.board_status.get(winning_condition[0])
            b = self.board_status.get(winning_condition[1])
            c = self.board_status.get(winning_condition[2])
            
            if a=='' and b=='' and c=='':
                continue

            if a==b and b==c:
                exists_winner = True
                break
        
        if exists_winner:
            return 'G'
        else:
            if '' not in self.board_status.values():
                return 'E'
            else:
                return 'C'

    
    def start(self):        
        self.render_instructions()
        
        while True:
            self.current_player.play_turn()
            self.render_board_status()
            result = self.check_board()
            if result == 'G':
                print(f'Ganó el jugador {self.current_player}')
                break
            else:
                if result == 'E':
                    print('Empate')
                    break
                else:
                    self.current_player = self.player_2 if self.current_player==self.player_1 else self.player_1
                    continue
            