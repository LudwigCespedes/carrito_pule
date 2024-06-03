from car_park_puzzle.game_board import Board, Car
from map import map1, map2, map3, map4, map5, map6, map7, map8, map9
import time
import os
import psutil
import tracemalloc

def main():
    while True:
        mode = input("¿Qué modo de juego quieres jugar (JUGADOR o BOT)? ")
        if mode.upper() == "JUGADOR":
            maps = int(input("¿Qué mapa quieres jugar (1-9)? "))
            if maps == 1:
                game = map1()
            elif maps == 2:
                game = map2()
            elif maps == 3:
                game = map3()
            elif maps == 4:
                game = map4()
            elif maps == 5:
                game = map5()
            elif maps == 6:
                game = map6()
            elif maps == 7:
                game = map7()
            elif maps == 8:
                game = map8()
            elif maps == 9:
                game = map9()
            else:
                print("Mapa no válido. Seleccione nuevamente.")
                continue

            game.display_board()

            while True:
                car_id = input("Ingresa el ID del coche a mover: ")
                direction = input("Ingresa la dirección (A, D, W, S): ")
                steps = int(input("Ingresa el número de pasos: "))
                game.move_car(car_id, direction, steps)
                game.display_board()

                if game.check_victory('A', 2, 8):  # Ajustar según la posición de la victoria en cada mapa
                    print("¡Has ganado!")
                    break

        elif mode.upper() == "BOT":
            maps = int(input("¿Qué mapa quieres jugar (1-9)? "))
            if maps == 1:
                start_time = time.time()
                tracemalloc.start()
                game = map1()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                
  
                
            elif maps == 2:
                start_time = time.time()
                tracemalloc.start()
                game = map2()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])            
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()            
            
            
            elif maps == 3:
                tracemalloc.start()
                start_time = time.time()
                game = map3()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()            
            
            elif maps == 4:
                tracemalloc.start()
                start_time = time.time()
                game = map4()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
            elif maps == 5:
                tracemalloc.start()
                start_time = time.time()
                game = map5()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop() 
            elif maps == 6:
                tracemalloc.start()
                start_time = time.time()
                game = map6()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
            elif maps == 7:
                tracemalloc.start()
                start_time = time.time()
                game = map7()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop() 
 
            elif maps == 8:
                tracemalloc.start()
                start_time = time.time()
                game = map8()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
 
            elif maps == 9:
                tracemalloc.start()
                start_time = time.time()
                game = map9()
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()

            else:
                print("Mapa no válido. Seleccione nuevamente.")
                continue

            game.display_board()

            game.dfs('A', 2, 8)  # Ajustar según la posición de la victoria en cada mapa
        else:
            print("Error!!!!!!!")
            print("Seleccione nuevamente")
            continue

if __name__ == "__main__":
    main()





