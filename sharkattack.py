import turtle
bob = turtle.Turtle()
turtle.colormode(255)
from myfunctions import*
turtle.bgcolor("black")
bob.speed(0)
for times in range(10):
    bob.width(400)
    bob.penup()
    bob.goto(-880,320)
    bob.pendown()
    bob.color(102,255,255)
    bob.forward(1750)

for times in range(10):
    bob.width(200)
    bob.penup()
    bob.goto(-880,180)
    bob.pendown()
    bob.color(204,255,255)
    bob.forward(1750)

for times in range(10):
    bob.width(110)
    bob.penup()
    bob.goto(-880,230)
    bob.pendown()
    bob.color(153,255,255)
    bob.forward(1800)

for times in range(10):
    bob.width(100)
    bob.penup()
    bob.goto(-880,100)
    bob.pendown()
    bob.color(204,255,229)
    bob.forward(1750)

for times in range(10):
    bob.width(190)
    bob.penup()
    bob.goto(-880,10)
    bob.pendown()
    bob.color(220,230,225)
    bob.forward(1750)

for times in range(10):
    bob.width(450)
    bob.penup()
    bob.goto(-880,-300)
    bob.pendown()
    bob.color(0,128,255)
    bob.forward(1750)

for times in range(1):
    bob.width(0)
    bob.color(255,255,102)
    bob.begin_fill()
    bob.penup()
    bob.goto(-300,180)
    bob.pendown()
    bob.circle(100)
    bob.end_fill()

bob.color(51,25,0)
bob.penup()
bob.goto(-100,25)
bob.pendown()

bob.begin_fill()
bob.forward(200)
bob.right(90)

bob.forward(100)
bob.right(90)

bob.forward(200)
bob.right(90)

bob.forward(100)
bob.right(90)

bob.right(90)
bob.forward(100)
bob.end_fill()

bob.begin_fill()
bob.right(140)
bob.forward(130)
bob.right(130)
bob.forward(100)
bob.end_fill()

bob.forward(184)
bob.right(90)
bob.forward(100)

bob.begin_fill()
bob.left(140)
bob.forward(131)
bob.left(130)
bob.forward(100)
bob.end_fill()

bob.forward(90)
bob.right(90)
bob.begin_fill()
bob.forward(200)
bob.color(255,255,255)
for times in range(3):
    bob.right(120)
    bob.forward(140)
    bob.end_fill()

bob.penup()
bob.goto(0,-200)
bob.pendown()
bob.right(80)
c = (125,125,125)
fish(bob,3,50,c)
a = 360/3
bob.begin_fill()
for times in range(3):
    bob.color(c)
    bob.left(a)
    bob.forward(50)
    
bob.end_fill()

bob.penup()
bob.goto(200,-200)
bob.pendown()
c = (125,125,125)
fish(bob,3,50,c)
a = 360/3
bob.begin_fill()
for times in range(3):
    bob.color(c)
    bob.left(a)
    bob.forward(50)
    
bob.end_fill()

bob.penup()
bob.goto(220,-100)
bob.pendown()
c = (125,125,125)
fish(bob,3,50,c)
a = 360/3
bob.begin_fill()
for times in range(3):
    bob.color(c)
    bob.left(a)
    bob.forward(50)
    
bob.end_fill()

bob.penup()
bob.goto(-200,-100)
bob.pendown()
c = (125,125,125)
fish(bob,3,50,c)
a = 360/3
bob.begin_fill()
for times in range(3):
    bob.color(c)
    bob.left(a)
    bob.forward(50)
    
bob.end_fill()

bob.penup()
bob.goto(-100,-200)
bob.pendown()
c = (125,125,125)
fish(bob,3,50,c)
a = 360/3
bob.begin_fill()
for times in range(3):
    bob.color(c)
    bob.left(a)
    bob.forward(50)
    
bob.end_fill()

