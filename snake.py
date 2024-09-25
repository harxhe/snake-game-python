from turtle import Turtle
import random

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:

            new_segment=Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.segments[0].color('grey')
    
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    
    
    def extend_snake(self):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        x_cor=self.segments[len(self.segments)-1].xcor()
        y_cor=self.segments[len(self.segments)-1].ycor()
        new_segment.goto(x_cor,y_cor)
        self.segments.append(new_segment)

  
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.segments[0].setheading(270)
    def right(self):
        self.segments[0].setheading(0)
    def left(self):
        self.segments[0].setheading(180)
    

    def snake_bite(self):
        for n in range(3,len(self.segments)-1):
            if self.head.xcor()==self.segments[n].xcor() and self.head.ycor()==self.segments[n].ycor():
                return True