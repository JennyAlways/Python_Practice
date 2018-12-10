import turtle
t = turtle.Pen()
t.pencolor("blue")
#turtle.bgcolor("black")

color=["orange","black","green","blue","red","purple"]
place=-1
left=0

for a in range(100):
    #print left

    #print place 

    t.pencolor(color[a%6])
    

    t.forward(a)
    t.left(90)

#another project
    #for a in range(3):
     #   t.forward(100)
     #   t.left(120)

turtle.done()







