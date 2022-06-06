class Player:    
    
    def __init__(self, id):
        self.id = id
    
    def play_turn(self):
        return input(f'\nJugador {self.id} >>: ').lower()
        