from turtle import Screen, Turtle,time
from snake import Snake
import random
from food import Food
from scoreboard import Scoreboard
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

tom= Snake()
food=Food()
board=Scoreboard()


screen.listen()
screen.onkey(tom.up, "w")
screen.onkey(tom.down, "s")
screen.onkey(tom.right, "d")
screen.onkey(tom.left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2) 
    tom.move()

    #Checking collisons with food
    if tom.head.distance(food) < 20:
       # print("Yummy")
        food.spawn_food()
        tom.extend_snake()
        board.increase_score()

    #Checking collision with wall
    if tom.head.xcor()>280 or  tom.head.xcor() < -280 or  tom.head.ycor() > 280 or  tom.head.ycor() < -280:
        board.game_over()
        game_is_on = False

    #Checking collision with its own body
    if tom.snake_bite()==True:
        board.game_over()
        game_is_on=False
screen.update()
screen.exitonclick()
