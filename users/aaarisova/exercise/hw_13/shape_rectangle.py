class Rectangle(Shape):

    def __init__(self, width, height):
       #? super().__init__()  # Вызываем конструктор базового класса Shape
        if width <= 0 or height <= 0:
            raise ValueError('Ширина и высота должны быть > 0')
            #return None, 'Ширина и высота должны быть > 0')
        self.width = float(width)
        self.height = float(height)
  
    def area(self):
        return self.width * self.height  
        
    
    def perimeter(self):
        return 2 * (self.width + self.height) 
