class Shape:
    colours = ("red", "blue", "black", "white")
    type = "shape"
    
    def __init__(self, colour):        
        if colour in Shape.colours:
            self._colour = colour
        else:
            raise ValueError("Invalid colour value")

    @property
    def colour(self):
        return self._colour    
    
    @property
    def type(self):
        return self.type

    @property
    def perimeter(self):
        pass

    @property
    def area(self):
        pass



    