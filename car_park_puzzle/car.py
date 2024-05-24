class Car:
    """
    A class for modeling a car 
    """
    def __init__(self, id, length, orientation, row, col):

        """
        Initializes the car object 
        input: 
            id, length or area,  orientation ( H = horizontal or V = vertical) , row, col

        """


        self.id = id  # id for the car
        self.length = length  # length for the car
        self.orientation = orientation  # orientation ( H = horizontal or V = vertical)
        self.row = row  # row
        self.col = col  # colunm 