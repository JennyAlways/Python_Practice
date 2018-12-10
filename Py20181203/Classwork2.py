import turtle

t=turtle.Pen()
t.pensize(10)

t.penup()
t.goto(-250,125)
t.pendown()
t.pencolor("blue")
t.circle(100)

t.penup()
t.goto(-125,0)
t.pendown()
t.pencolor("yellow")
t.circle(100)

t.penup()
t.goto(0,125)
t.pendown()
t.pencolor("black")
t.circle(100)

t.penup()
t.goto(125,0)
t.pendown()
t.pencolor("green")
t.circle(100)

t.penup()
t.goto(250,125)
t.pendown()
t.pencolor("red")
t.circle(100)

t.penup()
t.goto(300,300)
t.pendown()
t.circle(100,180)


turtle.done()






