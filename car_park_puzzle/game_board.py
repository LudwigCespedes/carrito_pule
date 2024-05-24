class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [['.' for _ in range(row)] for _ in range(col)]
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
        print()

    def move_car(self, car_id, direction, steps):
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

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def check_victory(self, car_id, exit_row, exit_col):
        car = self.cars[car_id]
        if car.orientation == 'H' and car.col + car.length - 1 == exit_col and car.row == exit_row:
            return True
        return False
