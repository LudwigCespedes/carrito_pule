from car_park_puzzle.game_board import Board , Car

"""
        car_id = input("Ingresa el ID del coche a mover: ")
        direction = input("Ingresa la dirección (A, D, W, S): ")
        steps = int(input("Ingresa el número de pasos: "))

        game.move_car(car_id, direction, steps)

        if game.check_victory('1', 2, 5):
            print("¡Has ganado!")
            break
"""

def main():
    tablero = Board(5, 7)

    # Agregar los coches
    tablero.add_car(Car('A', 2, 'H', 2, 0))
    #tablero.add_car(Car('1', 2, 'V', 2, 5))
    tablero.add_car(Car('2', 2, 'V', 3, 0))
    tablero.add_car(Car('3', 2, 'V', 2, 3))
    tablero.add_car(Car('4', 2, 'H', 4, 2))
    tablero.add_car(Car('5', 2, 'V', 2, 5))
    tablero.add_car(Car('6', 2, 'V', 3, 6))
    tablero.add_car(Car('7', 2, 'V', 1, 6))
    tablero.add_car(Car('8', 2, 'H', 0, 1))
    tablero.add_car(Car('9', 2, 'H', 0, 5))
    tablero.add_car(Car('S', 2, 'H', 1, 2))
    tablero.add_car(Car('C', 2, 'H', 3, 1))
    tablero.add_car(Car('B', 2, 'H', 4, 4))

    # Mostrar el tablero inicial
    tablero.display_board()

    # Ejecutar BFS para encontrar la solución
    t=tablero.bfs('A', 2, 6)
    tablero.display_board()
    print(t)  
   
"""
        car_id = input("Ingresa el ID del coche a mover: ")
        direction = input("Ingresa la dirección (A, D, W, S): ")
        steps = int(input("Ingresa el número de pasos: "))

        game.move_car(car_id, direction, steps)

        if game.check_victory('1', 2, 5):
            print("¡Has ganado!")
            break"""




if __name__ == "__main__":
    main()


