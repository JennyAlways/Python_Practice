import turtle

t = turtle.Turtle()

t.speed(10)

numOfLines = 60

for i in range(numOfLines):
    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(50)
    t.right(30)
    
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    
    t.right(360/numOfLines)
    
turtle.done()
