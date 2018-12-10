import turtle

t=turtle.Pen()

turtle.bgcolor("black")
colorDict={"gold":[0.93,0.79,0],"blueGreen":[0.3,1,0.7],"purple":[0.6,0.15,0.8]}

color=["gold","blueGreen","purple"]

for i in range(200):
    t.pencolor(colorDict[color[i%3]])
    t.forward(i)
    t.left(61)
    
turtle.done()


#How to get items out of the list: color[1]
