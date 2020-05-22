import random
from board import Board

class Game:
    """ Class for the game representation """

    def __init__(self):
        """ (Game) -> NoneType
        Create the new game atribute """

        self._board = Board()

    def _move_comp_person(self):
        """ (Game) -> NoneType
        Simulate the person movement """

        move_tuple = random.choice(self._board.possible())
        self._board[move_tuple] = 'x'
    
    def _move_person(self):
        print('Free position:', *self._board.possible())
        while True:
            tupl = input('Enter your movement as "0 2" (choose of free position): ')
            try:
                move_tuple = tuple(map(int, tupl.split()))
                if move_tuple not in self._board.possible():
                    raise ValueError
                self._board[move_tuple] = 'x'
                break
            except Exception:
                print("You entered the wrong number. Try again")

    def _play(self, func):
        """ (Game) -> NoneType
        Simulate the game tic-tac-toe with the computer system
        and computer person (random choice) or person """

        func()
        print('\nhuman movement:\n')
        print(self._board)

        while self._board.possible() != []:
            self._board.move_computer()
            print('\ncomputer movement:\n')
            print(self._board)
            if self._board.check_win():
                print('\nwinner is computer')
                return

            func()
            print('\nhuman movement:\n')
            print(self._board)
            if self._board.check_win():
                print('\nwinner is human')
                return
        print('\nwinner is friendship :)')

    def play_simulation(self):
        """ (Game) -> NoneType
        Simulate the game tic-tac-toe with the computer system
        and computer person (random choice) """
        self._play(self._move_comp_person)

    def play(self):
        """ (Game) -> NoneType
        Run the game tic-tac-toe with the computer system
        and person """
        self._play(self._move_person)




if __name__ == "__main__":
    game = Game()
    game.play()
