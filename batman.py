#author CJP 03/24/2022
#import turtle
import turtle
#creates window
window = turtle.Screen()
window.setup(500, 500)
window.title("Lab 3")
window.bgcolor("black")
#gives turtle name
ted = turtle.Turtle()
ted.shape("turtle")
ted.pencolor("gold")

#moves turtle
for x in range(3):
    ted.left(30)
    ted.forward(50)
    ted.left(30)
    ted.right(40)
    ted.forward(80)
    ted.left(50)

#window stays opebn
window.mainloop()
