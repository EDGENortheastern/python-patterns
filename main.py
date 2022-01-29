import turtle
from random import randint

wn = turtle.Screen()
wn.setup(500,350)
wn.colormode(255)
my_turtle=turtle.Turtle()
my_turtle.speed(10)


for i in range(0,6):
  for i in range(0,4):
    my_turtle.forward(100)
    my_turtle.right(90)
  my_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
  my_turtle.circle(70)  
  my_turtle.right(60)

wn.mainloop()