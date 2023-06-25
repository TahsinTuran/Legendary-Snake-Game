from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.which()

    def refresh(self):
        self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 260, 20))

    def which(self):
        if random.randint(0, 10) == 2:
            self.color("red")
            self.shapesize(0.8,0.8)
            self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 260, 20))

        else:
            self.color("blue")
            self.shapesize(0.5,0.5)
            self.refresh()
        
    