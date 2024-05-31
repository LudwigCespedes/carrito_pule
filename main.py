from car_park_puzzle.car import Car
from car_park_puzzle.game_board import Board
from car_park_puzzle.gui.main_gui import *
from car_park_puzzle.algoritmos.dfs import BFS
#main()
def main():
    CAR1 = Car('1', 2, 'H', 2, 2)
    CAR2 = Car('2', 2, 'H', 3, 3)
    CAR3 = Car('3', 3, 'V', 0, 0)
    CAR4 = Car('4', 2, 'H', 0, 3)
    CAR5 = Car('5', 2, 'V', 3, 1)
    CAR6 = Car('7', 5, 'H', 5, 0)
    game = Board(row=6, col=6)
    game.add_car(CAR1)
    game.add_car(CAR2)  # Coche objetivo
    game.add_car(CAR3)
    game.add_car(CAR3)
    game.add_car(CAR4)
    game.add_car(CAR5)
    game.add_car(CAR6)


    while True:
        game.display_board()
        print(game.get_movable_cars())
        print("Estado inicial del tablero:")
        game.display_board()

        BFS(game,"1",exit_row=2, exit_col=5).bfs()
        
        
   

        car_id = input("Ingresa el ID del coche a mover: ")
        direction = input("Ingresa la dirección (A, D, W, S): ")
        steps = int(input("Ingresa el número de pasos: "))

        game.move_car(car_id, direction, steps)

        if game.check_victory('1', 2, 5):
            print("¡Has ganado!")
            break




if __name__ == "__main__":
    main()