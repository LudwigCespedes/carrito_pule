import heapq
from collections import deque

class Car:
    """
    A class for modeling a car 
    """
    def __init__(self, id, length, orientation, row, col, movable = True):
        self.id = id
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.movable = movable


class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [['.' for _ in range(col)] for _ in range(row)]
        self.cars = {}

    def add_car(self, car):
        self.cars[car.id] = car
        if car.orientation == 'H':
            for i in range(car.length):
                self.board[car.row][car.col + i] = car.id
        elif car.orientation == 'V':
            for i in range(car.length):
                self.board[car.row + i][car.col] = car.id

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        
    def move_car(self, car_id, direction, steps):
        car = self.cars[car_id]
        if not car.movable:
            print(f"La roca {car_id} no se puede mover")
            return
        
        if car.orientation == 'H':
            if direction == 'A':
                if car.col - steps >= 0 and all(self.board[car.row][car.col - i] == '.' for i in range(1, steps + 1)):
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = '.'
                    car.col -= steps
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = car.id
            elif direction == 'D':
                if car.col + car.length + steps - 1 < self.col and all(self.board[car.row][car.col + car.length - 1 + i] == '.' for i in range(1, steps + 1)):
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = '.'
                    car.col += steps
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = car.id
        elif car.orientation == 'V':
            if direction == 'W':
                if car.row - steps >= 0 and all(self.board[car.row - i][car.col] == '.' for i in range(1, steps + 1)):
                    for i in range(car.length):
                        self.board[car.row + i][car.col] = '.'
                    car.row -= steps
                    for i in range(car.length):
                        self.board[car.row + i][car.col] = car.id
            elif direction == 'S':
                if car.row + car.length + steps - 1 < self.row and all(self.board[car.row + car.length - 1 + i][car.col] == '.' for i in range(1, steps + 1)):
                    for i in range(car.length):
                        self.board[car.row + i][car.col] = '.'
                    car.row += steps
                    for i in range(car.length):
                        self.board[car.row + i][car.col] = car.id

    def check_victory(self, car_id, exit_row, exit_col):
        car = self.cars[car_id]
        if car.orientation == 'H':
            if car.col + car.length - 1 == exit_col and car.row == exit_row:
                return True
        elif car.orientation == 'V':
            if car.row + car.length - 1 == exit_row and car.col == exit_col:
                return True
        return False

    def get_movable_cars(self):
        movable_cars = []
        for car_id, car in self.cars.items():
            if not car.movable:
                continue
            if car.orientation == 'H':
                for steps in range(1, car.col + 1):
                    if all(self.board[car.row][car.col - i] == '.' for i in range(1, steps + 1)):
                        movable_cars.append([car_id, 'A', steps])
                    else:
                        break
                for steps in range(1, self.col - (car.col + car.length) + 1):
                    if all(self.board[car.row][car.col + car.length - 1 + i] == '.' for i in range(1, steps + 1)):
                        movable_cars.append([car_id, 'D', steps])
                    else:
                        break
            elif car.orientation == 'V':
                for steps in range(1, car.row + 1):
                    if all(self.board[car.row - i][car.col] == '.' for i in range(1, steps + 1)):
                        movable_cars.append([car_id, 'W', steps])
                    else:
                        break
                for steps in range(1, self.row - (car.row + car.length) + 1):
                    if all(self.board[car.row + car.length - 1 + i][car.col] == '.' for i in range(1, steps + 1)):
                        movable_cars.append([car_id, 'S', steps])
                    else:
                        break
        return movable_cars

    def copy_board(self):
        new_board = Board(self.row, self.col)
        new_board.board = [row[:] for row in self.board]
        new_board.cars = {car_id: Car(car.id, car.length, car.orientation, car.row, car.col) for car_id, car in self.cars.items()}
        return new_board

    def bfs(self, target_car_id, exit_row, exit_col):
        initial_state = self.copy_board()
        frontier = deque([(initial_state, [])])
        visited = set()

        while frontier:
            current_state, path = frontier.popleft()

            if current_state.check_victory(target_car_id, exit_row, exit_col):
                print(f"Ganaste. Ruta: {path}")
                return path

            current_state_str = str(current_state.board)
            if current_state_str in visited:
                continue

            visited.add(current_state_str)
            for move in current_state.get_movable_cars():
                new_state = current_state.copy_board()
                new_state.move_car(move[0], move[1], move[2])
                new_path = path + [move]
                frontier.append((new_state, new_path))

        print("No se encontró solución.")
        return None
    
    def dfs(self, target_car_id, exit_row, exit_col,max_depth=10):
        initial_state = self.copy_board()
        frontier = [(initial_state, [], 0)]
        visited = set()
        #print(frontier.pop())
        while frontier:
            current_state, path, depth = frontier.pop()
            if depth > max_depth:
                continue
            if current_state.check_victory(target_car_id, exit_row, exit_col):
                print(f"Ganaste. Ruta: {path}")
                return path

            current_state_str = str(current_state.board)
            if current_state_str in visited:
                continue

            visited.add(current_state_str)
            for move in current_state.get_movable_cars():
                new_state = current_state.copy_board()
                new_state.move_car(move[0], move[1], move[2])
                new_path = path + [move]
                frontier.append((new_state, new_path, depth+1))

        print("No se encontró solución.")
        return None

    def heuristic_manhattan(self, car, exit_row, exit_col):
        if car.orientation == 'H':
            return abs(exit_row - car.row) + abs(exit_col - (car.col + car.length - 1))
        elif car.orientation == 'V':
            return abs(exit_row - (car.row + car.length - 1)) + abs(exit_col - car.col)

    def heuristic_euclidean(self, car, exit_row, exit_col):
        if car.orientation == 'H':
            return ((exit_row - car.row)**2 + (exit_col - (car.col + car.length - 1))**2)**0.5
        elif car.orientation == 'V':
            return ((exit_row - (car.row + car.length - 1))**2 + (exit_col - car.col)**2)**0.5

    def heuristic_blocking_cars(self, car, exit_row, exit_col):
        blocking_count = 0
        if car.orientation == 'H':
            for col in range(car.col + car.length, self.col):
                if self.board[car.row][col] != '.':
                    blocking_count += 1
        elif car.orientation == 'V':
            for row in range(car.row + car.length, self.row):
                if self.board[row][car.col] != '.':
                    blocking_count += 1
        return blocking_count

    def heuristic_weighted_manhattan(self, car, exit_row, exit_col):
        blocking_cars = self.heuristic_blocking_cars(car, exit_row, exit_col)
        return self.heuristic_manhattan(car, exit_row, exit_col) + blocking_cars

    def heuristic_movement_distance(self, car, exit_row, exit_col):
        if car.orientation == 'H':
            return abs(exit_col - (car.col + car.length - 1))
        elif car.orientation == 'V':
            return abs(exit_row - (car.row + car.length - 1))

    def combined_heuristics(self, car, exit_row, exit_col, heuristics = ['manhattan','euclidean','blocking_cars',"weighted_manhattan",'movement_distance']):
        total_cost = 0
        for heuristic in heuristics:
            if heuristic == 'manhattan':
                total_cost += self.heuristic_manhattan(car, exit_row, exit_col)
            elif heuristic == 'euclidean':
                total_cost += self.heuristic_euclidean(car, exit_row, exit_col)
            elif heuristic == 'blocking_cars':
                total_cost += self.heuristic_blocking_cars(car, exit_row, exit_col)
            elif heuristic == 'weighted_manhattan':
                total_cost += self.heuristic_weighted_manhattan(car, exit_row, exit_col)
            elif heuristic == 'movement_distance':
                total_cost += self.heuristic_movement_distance(car, exit_row, exit_col)
        return total_cost

    def a_star(self, target_car_id, exit_row, exit_col, heuristics):
        initial_state = self.copy_board()
        frontier = []
        heapq.heappush(frontier, (0, 0, initial_state, []))
        visited = set()
        state_id = 0

        while frontier:
            cost, _, current_state, path = heapq.heappop(frontier)

            if current_state.check_victory(target_car_id, exit_row, exit_col):
                print(f"Ganaste. Ruta: {path}")
                return path

            current_state_str = str(current_state.board)
            if current_state_str in visited:
                continue

            visited.add(current_state_str)
            for move in current_state.get_movable_cars():
                new_state = current_state.copy_board()
                new_state.move_car(move[0], move[1], move[2])
                new_path = path + [move]
                heuristic_cost = new_state.combined_heuristics(self.cars[target_car_id], exit_row, exit_col, heuristics)
                total_cost = cost + 1 + heuristic_cost
                state_id += 1
                heapq.heappush(frontier, (total_cost, state_id, new_state, new_path))

        print("No se encontró solución.")
        return None
 