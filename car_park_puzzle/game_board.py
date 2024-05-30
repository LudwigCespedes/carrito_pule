from car import Car 
from collections import deque
class Board:
    def __init__(self, row, col):
        """
        Initializes a game board with the given number of rows and columns.

        :param row: Number of rows in the board.
        :param col: Number of columns in the board.
        """

        self.row = row
        self.col = col
        self.board = [['.' for _ in range(col)] for _ in range(row)]
        self.cars = {}

    def add_car(self, car):
        """
        Adds a car to the board and places it at the specified position based on its orientation.

        :param car: An object representing the car with attributes id, orientation, length, row, and col.
        """
        self.cars[car.id] = car
        # Check if the car can be placed without exceeding boundaries
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
        """
        Moves a car on the board in the specified direction by the specified number of steps.

        :param car_id: The identifier of the car to be moved.
        :param direction: The direction to move the car ('A' for left, 'D' for right, 'W' for up, 'S' for down).
        :param steps: The number of steps to move the car.
        """

        car = self.cars[car_id]
        if car.orientation == 'H':
            if direction == 'A':
                if car.col - steps >= 0 and all(self.board[car.row][car.col - i] == '.' for i in range(1, steps + 1)):
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = '.'
                    car.col -= steps
                    for i in range(car.length):
                        self.board[car.row][car.col + i] = car.id
            elif direction == 'D':
                if car.col + car.length + steps - 1 < self.row and all(self.board[car.row][car.col + car.length - 1 + i] == '.' for i in range(1, steps + 1)):
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



#    def check_victory(self, car_id, exit_row, exit_col):
#        car = self.cars[car_id]
#        if car.orientation == 'H' and car.col + car.length - 1 == exit_col and car.row == exit_row:
#            return True
#       return False
    
    def check_victory(self, car_id, exit_row, exit_col):
        """
        Checks if the specified car has reached the exit position on the board.

        :param car_id: The identifier of the car to check.
        :param exit_row: The row of the exit position.
        :param exit_col: The column of the exit position.
        :return: True if the car has reached the exit position, False otherwise.
        """
        car = self.cars[car_id]
        
        if car.orientation == 'H':
            if car.col + car.length - 1 == exit_col and car.row == exit_row:
                return True
        elif car.orientation == 'V':
            if car.row + car.length - 1 == exit_row and car.col == exit_col:
                return True
        
        return False
    def get_movable_cars(self):
        """
        Returns a dictionary of cars that can be moved with the possible directions and steps.
        The keys are car IDs and the values are lists of tuples (direction, max_steps).

        :return: Dictionary of movable cars with possible directions and maximum steps.
        """
        movable_cars = {}

        for car_id, car in self.cars.items():
            directions = []

            if car.orientation == 'H':
                # Check left ('A')
                max_left_steps = 0
                for step in range(1, car.col + 1):
                    if self.board[car.row][car.col - step] == '.':
                        max_left_steps = step
                    else:
                        break
                if max_left_steps > 0:
                    directions.append(('A', max_left_steps))

                # Check right ('D')
                max_right_steps = 0
                for step in range(1, self.col - (car.col + car.length) + 1):
                    if self.board[car.row][car.col + car.length - 1 + step] == '.':
                        max_right_steps = step
                    else:
                        break
                if max_right_steps > 0:
                    directions.append(('D', max_right_steps))

            elif car.orientation == 'V':
                # Check up ('W')
                max_up_steps = 0
                for step in range(1, car.row + 1):
                    if self.board[car.row - step][car.col] == '.':
                        max_up_steps = step
                    else:
                        break
                if max_up_steps > 0:
                    directions.append(('W', max_up_steps))

                # Check down ('S')
                max_down_steps = 0
                for step in range(1, self.row - (car.row + car.length) + 1):
                    if self.board[car.row + car.length - 1 + step][car.col] == '.':
                        max_down_steps = step
                    else:
                        break
                if max_down_steps > 0:
                    directions.append(('S', max_down_steps))

            if directions:
                movable_cars[car_id] = directions

        return movable_cars

    def generate_successors(self):
        successors = []
        movable_cars = self.get_movable_cars()

        for car_id, moves in movable_cars.items():
            for direction, max_steps in moves:
                for steps in range(1, max_steps + 1):
                    new_board = self.clone()
                    new_board.move_car(car_id, direction, steps)
                    successors.append(new_board)
        
        return successors
    
    def clone(self):
        new_board = Board(self.row, self.col)
        for _, car in self.cars.items():
            new_car = Car(car.id, car.row, car.col, car.length, car.orientation)
            new_board.add_car(new_car)
        return new_board 

    def bfs(self, target_car_id, exit_row, exit_col):
        initial_state = self.clone()
        queue = deque([initial_state])
        visited = set()
        visited.add(self.board_to_tuple())

        while queue:
            current_board = queue.popleft()

            if current_board.check_victory(target_car_id, exit_row, exit_col):
                return current_board  # Or return the path to reach this state

            successors = current_board.generate_successors()
            for successor in successors:
                board_tuple = successor.board_to_tuple()
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(successor)

        return None

    def board_to_tuple(self):
        return tuple(tuple(row) for row in self.board)   
