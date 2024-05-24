from car_park_puzzle.car import Car
from car_park_puzzle.game_board import Board

def main():
    game = Board(row=6, col=6)
    game.add_car(Car('X', 2, 'H', 2, 2))  # Coche objetivo
    game.add_car(Car('A', 3, 'V', 0, 0))
    game.add_car(Car('B', 2, 'H', 0, 3))
    game.add_car(Car('C', 2, 'V', 3, 1))

    while True:
        game.display_board()
        car_id = input("Ingresa el ID del coche a mover: ")
        direction = input("Ingresa la dirección (A, D, W, S): ")
        steps = int(input("Ingresa el número de pasos: "))

        game.move_car(car_id, direction, steps)

        if game.check_victory('X', 2, 5):
            print("¡Has ganado!")
            break

if __name__ == "__main__":
    main()