
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
    
    def dfs1(self, target_car_id, exit_row, exit_col):
        initial_state = self.copy_board()
        frontier = [(initial_state, [])]
        visited = set()
        #print(frontier.popleft())
        while frontier:
            current_state, path = frontier.pop()

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

def dfs(board, car_id, goal_row, goal_col, max_depth=1000):
    stack = [(board, [], 0)]  # (tablero actual, movimientos, profundidad)
    visited = set()

    while stack:
        current_board, path, depth = stack.pop()

        if depth > max_depth:
            continue

        current_state = current_board.get_state()
        if current_state in visited:
            continue

        visited.add(current_state)

        if current_board.check_victory(car_id, goal_row, goal_col):
            print(f"¡Ganador! Carro {car_id} alcanzó la meta.")
            return path

        for move in current_board.get_possible_moves():
            next_board = current_board.copy()
            next_board.move_car(move)
            stack.append((next_board, path + [move], depth + 1))

    return None