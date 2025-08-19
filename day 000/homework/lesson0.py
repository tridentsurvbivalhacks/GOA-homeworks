from turtle import *

#we want to paint a house

#step 1 draw a square
speed(8)
width(7)
color("red")

begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#step 2 drawing a door
forward(70)
color("black")

begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()
#end of door

#step 3 drawing a roof
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
#end of roof

#step 4 drawing the windows
penup()
goto(30, 150)
pendown()

width(2)
begin_fill()
color("blue")

left(30)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
end_fill()
#end of main window

#window cross

color("black")

right(90)
forward(50)
right(90)
color("blue")
forward(25)
right(90)
forward(25)
right(90)
color("black")
forward(50)
#end of window #1

#window #2
penup()
goto(150, 150)
pendown()

color("blue")

begin_fill()
left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
left(180)
forward(25)
right(90)
#window cross
color("black")
forward(50)
right(180)
forward(25)
left(90)
forward(25)
left(180)
forward(50)
#end of the windows

#end of the house









exitonclick()
