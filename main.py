from car_park_puzzle.game_board import Board, Car
from map import map1, map2, map3, map4, map5, map6, map7, map8, map9, map10,map11, map12
import time
import os
import psutil
import tracemalloc

def main():
    while True:
        mode = input("¿Qué modo de juego quieres jugar (JUGADOR o BOT)? ")
        if mode.upper() == "JUGADOR":
            maps = int(input("¿Qué mapa quieres jugar (1-12)? "))
            if maps == 1:
                game = map1()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A', 5, 8):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
                
            elif maps == 2:
                game = map2()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A', 2, 6):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 3:
                game = map3()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory("A", 3, 6):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break                
            elif maps == 4:
                game = map4()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory("A", 2, 6):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break                
            elif maps == 5:
                game = map5()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory("A", 2, 6):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 6:
                game = map6()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory("A", 4, 8):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 7:
                game = map7()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A',3,8 ):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 8:
                game = map8()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A', 5,8):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 9:
                game = map9()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A',5, 8):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break
            elif maps == 10:
                game = map10()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A',6,14):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break 


            elif maps == 11:
                game = map11()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A',6,14):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break                            
            elif maps == 12:
                game = map12()
                game.display_board()
                while True:
                    car_id = input("Ingresa el ID del coche a mover: ")
                    direction = input("Ingresa la dirección (A, D, W, S): ")
                    steps = int(input("Ingresa el número de pasos: "))
                    game.move_car(car_id, direction, steps)
                    game.display_board()

                    if game.check_victory('A',9,14):  # Ajustar según la posición de la victoria en cada mapa
                        print("¡Has ganado!")
                        break              
            
            else:
                print("Mapa no válido. Seleccione nuevamente.")
                continue



        elif mode.upper() == "BOT":
            maps = int(input("¿Qué mapa quieres jugar (1-9)? "))
            BOT = input("¿Qué BOT quiere usar(DFS, BFS y A*)?")
            if maps == 1:
                start_time = time.time()
                tracemalloc.start()
                game = map1()
                if BOT.upper() == "DFS":
                    game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    game.a_star("A", 5, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 2, 6,)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 2, 6,)
                elif BOT.upper() == "A*":
                    game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 3, 6)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 3, 6)
                elif BOT.upper() == "A*":
                    game.a_star("A", 3, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 2, 6)
                elif BOT.upper() == "BFS":
                    game.bfs("A",  2, 6)
                elif BOT.upper() == "A*":
                    game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 2, 6)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 2, 6)
                elif BOT.upper() == "A*":
                    game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 4, 8)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 4, 8)
                elif BOT.upper() == "A*":
                    game.a_star("A", 4, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 3,8)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 3,8)
                elif BOT.upper() == "A*":
                    game.a_star("A", 3,8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    game.a_star("A",5,8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
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
                if BOT.upper() == "DFS":
                    game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    game.a_star("A", 5, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
            
            elif maps == 10:
                tracemalloc.start()
                start_time = time.time()
                game = map10()
                if BOT.upper() == "DFS":
                    game.dfs("A", 6,14)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 6,14)
                elif BOT.upper() == "A*":
                    game.a_star("A", 6,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()

            elif maps == 11:
                tracemalloc.start()
                start_time = time.time()
                game = map11()
                if BOT.upper() == "DFS":
                    game.dfs("A", 6,14)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 6,14)
                elif BOT.upper() == "A*":
                    game.a_star("A", 6,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
            
            elif maps == 12:
                tracemalloc.start()
                start_time = time.time()
                game = map12()
                if BOT.upper() == "DFS":
                    game.dfs("A", 9,14)
                elif BOT.upper() == "BFS":
                    game.bfs("A", 9,14)
                elif BOT.upper() == "A*":
                    game.a_star("A", 9,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
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

        else:
            print("Error!!!!!!!")
            print("Seleccione nuevamente")
            continue

import os

def generar_comparativa_movimientos(niveles, heuristicas, archivo_salida="comparativa_movimientos.txt"):
    resultados = []

    for i, map_func in enumerate(niveles):
        tablero = map_func()
        fila_resultados = [f'Nivel {i+1}']

        # Resolución con BFS
        try:
            solucion_bfs = tablero.bfs('A', tablero.fila_salida, tablero.columna_salida)
            movimientos_bfs = len(solucion_bfs) if solucion_bfs else -1
            print(f"Nivel {i+1} (BFS): {movimientos_bfs} movimientos")
        except Exception as e:
            movimientos_bfs = -1
            print(f"Error en BFS para nivel {i+1}: {e}")
        fila_resultados.append(movimientos_bfs)

        # Resolución con DFS
        try:
            solucion_dfs = tablero.dfs('A', tablero.fila_salida, tablero.columna_salida)
            movimientos_dfs = len(solucion_dfs) if solucion_dfs else -1
            print(f"Nivel {i+1} (DFS): {movimientos_dfs} movimientos")
        except Exception as e:
            movimientos_dfs = -1
            print(f"Error en DFS para nivel {i+1}: {e}")
        fila_resultados.append(movimientos_dfs)

        # Resolución con A* (con las heurísticas proporcionadas)
        try:
            solucion_a_star = tablero.a_star('A', tablero.fila_salida, tablero.columna_salida, heuristicas)
            movimientos_a_star = len(solucion_a_star) if solucion_a_star else -1
            print(f"Nivel {i+1} (A*): {movimientos_a_star} movimientos")
        except Exception as e:
            movimientos_a_star = -1
            print(f"Error en A* para nivel {i+1}: {e}")
        fila_resultados.append(movimientos_a_star)

        resultados.append(fila_resultados)

    # Generar el archivo de salida
    with open(archivo_salida, 'w') as file:
        # Escribir encabezados
        encabezados = ["Nivel", "Movimientos BFS", "Movimientos DFS", "Movimientos A*"]
        file.write("\t".join(encabezados) + "\n")

        # Escribir resultados
        for resultado in resultados:
            file.write("\t".join(map(str, resultado)) + "\n")

    print(f"Archivo '{archivo_salida}' generado con éxito.")

# Ejemplo de uso:
niveles = [map1(), map2(), map3(), map4(), map5(), map6(), map7(), map8(), map9(), map10()]
heuristicas = ['manhattan', 'blocking_cars', 'movement_distance']









if __name__ == "__main__":
    main()
    #generar_comparativa_movimientos(niveles, heuristicas)





