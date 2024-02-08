import turtle

HEXAGON_SIDE=50
HEXAGON_ANGLE=60
SQAURE_SIDE=90
SQAURE_ANGLE=90

"""defining setPos = setting the postion of turtle to move based on x and y coordinates """
def setPos(turta, x, y):
    turtle.penup() #moving pen without drawing
    turtle.goto(x, y) #moving to specific coordinates
    turtle.pendown() #draw based on position

"""defining hexagon shape to start drawing hexagon shape"""
def hexagon(turta, hexa_color, border_color):  # hexagon has color and border color
    turtle.fillcolor(hexa_color)
    turtle.pencolor(border_color)
    turtle.begin_fill()
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.forward(HEXAGON_SIDE)
    turtle.right(HEXAGON_ANGLE)
    turtle.end_fill()


"""defining square to start drawing square shape"""
def square(turta, square_color, border_color): #square has color and border color
    turtle.fillcolor(square_color)
    turtle.pencolor(border_color)
    turtle.begin_fill()
    turtle.forward(SQAURE_SIDE)
    turtle.right(SQAURE_ANGLE)
    turtle.forward(SQAURE_SIDE)
    turtle.right(SQAURE_ANGLE)
    turtle.forward(SQAURE_SIDE)
    turtle.right(SQAURE_ANGLE)
    turtle.forward(SQAURE_SIDE)
    turtle.right(SQAURE_ANGLE)
    turtle.end_fill()

"""defining circle to start drawing circle shape"""
def circle(turta, circle_color, border_color):#circle has color and border color
    turtle.fillcolor(circle_color)
    turtle.pencolor(border_color)
    turtle.begin_fill()
    turtle.circle(50) #size of circle
    turtle.end_fill()

"""defining pattern = choosing the pattern of each shape with the desired x and y coordinates to set their positions"""
def pattern(turtle, hexa_color, circle_color, square_color, border_color):
    setPos(turtle, -300, 60) # this sets postions for the hexagon with (-300,60)
    hexagon(turtle, hexa_color, border_color) #sets the color pattern
    setPos(turtle, -100, -30)# sets positon for circle
    circle(turtle, circle_color, border_color)#sets the color pattern
    setPos(turtle, 20, 60)#sets postion for square
    square(turtle, square_color, border_color)#sets the color pattern


    setPos(turtle, -200, -60)#sets postion for 2d hexagon
    hexagon(turtle, hexa_color, border_color)#sets the color pattern
    setPos(turtle, 0, -150)#sets postion for 2nd circle
    circle(turtle, circle_color, border_color)#sets the color pattern
    setPos(turtle, 150, -60)#sets postion for 2nd square
    square(turtle, square_color, border_color)#sets the color pattern



    setPos(turtle, -100, -200) #sets postion for 3rd hexagon 
    hexagon(turtle, hexa_color, border_color)#sets the color pattern
    setPos(turtle, 100, -290)#sets postion for 3rd circle
    circle(turtle, circle_color, border_color)#sets the color pattern
    setPos(turtle, 260, -200)#sets postion for 3rd square
    square(turtle, square_color, border_color)#sets the color pattern

"""calling in the main for user input of colors and border color"""
def main():
    hexa_color = input("Enter the color of hexagon: ")
    circle_color = input("Enter the color of circle: ")
    square_color = input("Enter the color of square: ")
    border_color = input("Enter the color of shape borders: ")

    turta = turtle.Turtle()
    turtle.speed(2)  # setting the speed of the turtle coloring and drawing

    pattern(turta, hexa_color, circle_color, square_color, border_color) #pattern has 5 arguments for color of the shapes and border

    turtle.done()

main()