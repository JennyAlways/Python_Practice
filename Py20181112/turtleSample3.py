"""
Hexagon Flower
by Zijie James Chen
2017.10.19
"""

from turtle import *
speed(0)
pencolor('white')
bgcolor('black')

x = 0
up()

rt(45) 
fd(90) 
rt(135) 

down()
while x < 120:
    fd(200)     
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)

    rt(11.1111) 
    x = x+1
done()




