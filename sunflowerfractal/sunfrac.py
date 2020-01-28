from turtle import *
from math import *

# Based on C implementation

iter = 3000
diskRatio = .5

factor = .5 + sqrt(1.25)

(winWidth, winHeight) = screen.screensize()

x = winWidth/2.0

y = winHeight/2.0

maxRad = pow(iter,factor)/iter;
  
bgcolor("light blue")

for i in range(iter+1):
    r = pow(i,factor)/iter;
    
    if r/maxRad < diskRatio:
        setcolor(BLACK)
    else:
        setcolor(YELLOW)
 
    theta = 2*pi*factor*i;
    
    turtle.setposition(x + r*sin(theta), y + r*cos(theta))
    
    circle(10 * i/(1.0*iter))

done()

