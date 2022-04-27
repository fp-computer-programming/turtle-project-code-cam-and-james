
import turtle


#initialize method
ted = turtle.Turtle()

#size of pointer and pen
ted.turtlesize(.5)
ted.pensize(3)

#screen info
wn = turtle.Screen()
wn.bgcolor("black")



#color
def changecolor(color):
    ted.pencolor(color)
    ted.fillcolor(color)
def changeshape(shape):
    ted.shape(shape)
    
changecolor(wn.textinput("color", "enter a color now! "))
changeshape(wn.textinput("shape", "enter a shape man! "))



#begin filling color
ted.begin_fill()

#turn1
ted.left(90)   # turn pointer direction to left of 90'
ted.circle(45, 75) #draw circle of radius = 50 and 85'
ted.circle(26, 125)
ted.right(180) 

#turn 2
ted.circle(25, 150)
ted.right(7)
ted.forward(20) #draw forward line of 10 units

#turn 3
ted.right(90)
ted.circle(-65, 140)
ted.forward(45)
ted.right(110)

#turn 4
ted.circle(100, 29)
ted.circle(29, 100)
ted.left(50)
ted.forward(50)
ted.right(145)

#turn5
ted.forward(30)
ted.left(55)
ted.forward(5)

#reverse

#turn 5
ted.forward(5)
ted.left(55)
ted.forward(30)

#turn 4

ted.right(145)
ted.forward(50)
ted.left(50)
ted.circle(29, 100)
ted.circle(100, 29)

#turn 3
ted.right(90)
ted.right(20)
ted.forward(45)
ted.circle(-65, 140)

#turn 2
ted.right(90)
ted.forward(20)
ted.right(7)
ted.circle(25, 150)

#turn 1
ted.left(180)
ted.circle(26, 125)
ted.circle(45, 75)

import turtle
turtle.goto(0,-60)
turtle.color('Gold')
style = ('Arial', 50, 'italic')
turtle.write('BATMAN', font=style, align='center')
turtle.hideturtle()

import turtle

ron = turtle.Turtle()

 
def eyes(color, radius):
    ron.down()
    ron.fillcolor(color)
    ron.begin_fill()
    ron.circle(radius)
    ron.end_fill()
    ron.up()

def changecolor1(color):
    ron.pencolor(color)
    ron.fillcolor(color)
def changeshape1(shape):
    ron.shape(shape)
    
changecolor1(wn.textinput("color", "Ron is approaching.... what color should it be?!?"))
changeshape1(wn.textinput("shape", "Enter a shape! Do not make ron angry! "))
 
 
ron.fillcolor('red')
ron.begin_fill()
ron.circle(150)
ron.end_fill()
ron.up()
 
ron.goto(-50, 110)
eyes('white', 15)
ron.goto(-52, 112)
eyes('blue', 5)
ron.goto(50, 110)
eyes('white', 15)
ron.goto(52, 116)
eyes('blue', 5)
 
ron.goto(0, 75)
eyes('orange', 8)
 
ron.goto(-30, 95)
ron.down()
ron.right(90)
ron.circle(40, 180)
ron.up()




 
ron.hideturtle()

import turtle

van = turtle.Turtle()
def changecolor1(color):
    van.pencolor(color)
    van.fillcolor(color)
def changeshape1(shape):
    van.shape(shape)
    
changecolor1(wn.textinput("color", "The Great Eye of Mead. Ron or the Eye? Color?"))
changeshape1(wn.textinput("shape", "Enter a shape!  "))

van.penup()

van.goto(-90, -170)
van.pendown()
van.fillcolor("white")
van.begin_fill()
van.circle(80)
van.end_fill()
van.penup()


van.goto(-70,-130)
van.pendown()
van.fillcolor("green")
van.begin_fill()
van.circle(28)
van.end_fill()
van.penup()

van.goto(-70,-130)
van.pendown()
van.fillcolor("red")
van.begin_fill()
van.circle(20)
van.end_fill()
van.penup()
van.hideturtle()

import turtle
turtle.goto(0,-230)
turtle.color('Red')
style = ('Times New Roman', 50, 'italic')
turtle.write('THE GREAT EYE OF MEAD', font=style, align='center')
turtle.hideturtle()

#end the turtle method
turtle.done()

