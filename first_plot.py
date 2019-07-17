# coding: utf-8
from pylab import *
x = linspace((-5)*pi , 5*pi , 50)
plot(x,(-x),'b')
plot(x,(x),'b')
plot(x,sin(x),'g',linewidth = '2' )
plot(x,x*sin(x),'r',linewidth = '3' )
legend(['-x','x','sin(x)','x*sin(x)'], loc = 'upper right')
annotate('origin' , xy=(0,0))
xlim(-5*pi , 5*pi)
ylim(-5*pi , 5*pi)
show()