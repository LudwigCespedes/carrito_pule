class Board:
    def __init__(self, row, col):
        """
        Initializes a game board with the given number of rows and columns.

        :param row: Number of rows in the board.
        :param col: Number of columns in the board.
        """

        self.row = row
        self.col = col
        self.board = [['.' for _ in range(row)] for _ in range(col)]
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
        print()

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
