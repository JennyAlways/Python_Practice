import turtle

t=turtle.Pen()
turtle.bgcolor("black")

for i in range(240):
    t.pencolor((i/255.0,(255-i)/255.0,i/255.0))

    t.forward(i)
    t.left(70)

turtle.done()
