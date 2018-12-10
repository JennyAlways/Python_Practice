"""
Psychedelic Flower
by Zijie James Chen
2017.10.19
"""

from turtle import *
from random import randint

speed(0)
bgcolor('black')
x = 1
      
while x < 800:
      
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255) 
    
    pencolor(r,g,b) 
    fd(x)
    rt(90.911)
    
    
    x = x+1 

done()