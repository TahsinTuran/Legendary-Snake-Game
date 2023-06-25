from turtle import Turtle
segment_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
class Snake:


    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
         for segment in segment_POSTIONS:
            self.add_segment(segment)
    def add_segment(self, segment):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(segment)
        self.segments.append(new_segment)
    
    def extend(self):
            self.add_segment(self.segments[-1].position())

    def bigextend(self):
        self.add_segment(self.segments[-1].position())
        self.add_segment(self.segments[-1].position())
        self.add_segment(self.segments[-1].position())

    
    def move(self):
            for seg_num in range(len(self.segments) -1, 0, -1):
                newx = self.segments[seg_num - 1].xcor()
                newy = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(newx, newy)
            self.segments[0].forward(MOVE)
    def up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)


    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)     
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)     
