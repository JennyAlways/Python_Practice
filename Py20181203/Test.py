import turtle

t=turtle.Pen()

turtle.bgcolor("black")
t.pencolor("gold")
t.fillcolor("gold")

t.begin_fill()
for i in range(12):
	t.setheading(i*30)
	t.forward(200)
	t.left(150)
	t.forward(100)
	t.goto(0,0)
t.end_fill()

turtle.done()