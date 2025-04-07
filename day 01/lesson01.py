from turtle import *


#we want to paint a house

#step 1: draw a square
width(7)
color("orange")
forward(200)
left(90)
#drawing a window



forward(200)
left(90)

forward(200)
left(90)
#drawing a window


forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("grey")
begin_fill()

left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a window
color("yellow")
begin_fill()
penup()
right(-90)
forward(60)
right(-90)
right(90)
right(-30)
pendown()
forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)
end_fill()


exitonclick()