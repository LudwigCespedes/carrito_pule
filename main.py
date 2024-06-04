from car_park_puzzle.game_board import Board, Car
from map import map1, map2, map3, map4, map5, map6, map7, map8, map9, map10,map11, map12
import time
import os
import psutil
import tracemalloc
import pandas as pd

def metricas(nivel, algoritmo, tiempo_ejecucion, memoria_actual, memoria_maxima, ruta, tamaño_de_la_ruta):
    # Verificar si el archivo existe
    if os.path.exists("metricas.csv"):
        df = pd.read_csv("metricas.csv")
    else:
        df = pd.DataFrame(columns=["nivel", "algoritmo", "tiempo_ejecucion", "memoria_actual", "memoria_maxima", "ruta", "tamaño_de_la_ruta"])
    
    # Crear un nuevo DataFrame con los datos a agregar
    nuevo_dato = pd.DataFrame([{
        "nivel": nivel, 
        "algoritmo": algoritmo, 
        "tiempo_ejecucion": tiempo_ejecucion, 
        "memoria_actual": memoria_actual, 
        "memoria_maxima": memoria_maxima, 
        "ruta": ruta, 
        "tamaño_de_la_ruta": tamaño_de_la_ruta
    }])
    
    
    df = pd.concat([df, nuevo_dato], ignore_index=True)
    
    
    df.to_csv("metricas.csv", index=False)
    
    print(f"Archivo 'metricas.csv' actualizado con éxito.")

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
            maps = int(input("¿Qué mapa quieres jugar (1-12)? "))
            BOT = input("¿Qué BOT quiere usar(DFS, BFS y A*)?").upper()
            if maps == 1:
                start_time = time.time()
                tracemalloc.start()
                game = map1()
                if BOT.upper() == "DFS":
                    resul = game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    resul = game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    resul = game.a_star("A", 5, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
  
                
            elif maps == 2:
                start_time = time.time()
                tracemalloc.start()
                game = map2()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 2, 6,)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 2, 6,)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])            
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()            
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            
            elif maps == 3:
                tracemalloc.start()
                start_time = time.time()
                game = map3()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 3, 6)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 3, 6)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 3, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()            
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 4:
                tracemalloc.start()
                start_time = time.time()
                game = map4()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 2, 6)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A",  2, 6)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 5:
                tracemalloc.start()
                start_time = time.time()
                game = map5()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 2, 6)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 2, 6)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 2, 6,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))

            elif maps == 6:
                tracemalloc.start()
                start_time = time.time()
                game = map6()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 4, 8)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 4, 8)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 4, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))


            elif maps == 7:
                tracemalloc.start()
                start_time = time.time()
                game = map7()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 3,8)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 3,8)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 3,8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop() 
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 8:
                tracemalloc.start()
                start_time = time.time()
                game = map8()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A",5,8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 9:
                tracemalloc.start()
                start_time = time.time()
                game = map9()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 5, 8)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 5, 8)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 5, 8,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 10:
                tracemalloc.start()
                start_time = time.time()
                game = map10()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 6,14)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 6,14)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 6,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 11:
                tracemalloc.start()
                start_time = time.time()
                game = map11()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 6,14)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 6,14)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 6,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            elif maps == 12:
                tracemalloc.start()
                start_time = time.time()
                game = map12()
                if BOT.upper() == "DFS":
                    resul =game.dfs("A", 9,14)
                elif BOT.upper() == "BFS":
                    resul =game.bfs("A", 9,14)
                elif BOT.upper() == "A*":
                    resul =game.a_star("A", 9,14,heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance'])
                else:
                    print("Error")                
                end_time = time.time()
                print("El tiempo de ejecución es:", end_time - start_time, "segundos")
                print('RAM memory % used:', psutil.virtual_memory()[2])
                current, peak = tracemalloc.get_traced_memory()
                print(f"Consumo de memoria actual: {current / 10**6} MB")
                print(f"Consumo de memoria máximo: {peak / 10**6} MB")
                tracemalloc.stop()
                metricas(maps,BOT,tiempo_ejecucion=end_time - start_time,memoria_actual=current / 10**6,memoria_maxima=peak / 10**6,ruta= resul,tamaño_de_la_ruta=len(resul))
            else:
                print("Mapa no válido. Seleccione nuevamente.")
                continue

            game.display_board()

        else:
            print("Error!!!!!!!")
            print("Seleccione nuevamente")
            continue











if __name__ == "__main__":
    main()
    





