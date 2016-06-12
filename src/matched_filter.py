#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import math 


fc = 1			# Center frequency of operation
T = 100			# Sampling Frequency
t = np.linspace(0,100,T*20) # Time from start to stop
s = 10e3 		# Distance between the base station and mobile station (m)
d = np.arange(1,s)	# Point where the reflected path signal hits the ground (m)
hb = 20			# Height of base station (m)
hm = 1.5		# Height of mobile station (m)

# Distance travelled by direct line of sight signal
# Distance travelled by reflected signal

td = 1			# Time taken by the signal to travel direct path (s)
tr = 10			# Time taken by the signal to travel reflected path (s)

w = 2 * np.pi * fc
#w = math.radians(w1)
x = np.sin(w * t)	# Transmitted signal
#plt.plot(t,x)

y = np.sin(w*(t-td)) + np.sin(w*(t-tr))
#plt.plot(t,y)
#plt.show()

h = np.sin(w*(T-t)) 	# Response of the Matched Filter
#plt.plot(t,h)
#plt.show()

z = np.convolve(y,h)		# Matched Filter output
#print z.shape
plt.plot(z, label='simulated')
#plt.legend()
#plt.show()

# FINAL CALCULATED VALUES
cosT = np.cos(w*T) 
cost = np.cos(w*t)
costd = np.cos(w*td)
costr = np.cos(w*tr)

sinT = np.sin(w*T)
sint = np.sin(w*t)
sintd = np.sin(w*td)
sintr = np.sin(w*tr)

print 'cosT', cosT, 'costd', costd, 'costr', costr
#plt.plot(cost, label='cost')
#plt.show()

print 'sinT', sinT, 'sintd', sintd, 'sintr', sintr
#plt.plot(sint, label='sint')
#plt.legend()
#plt.show()

ad = cosT*cost*costd + sinT*sint*costd
bd = cosT*sint*sintd - sinT*cost*costd
gd = sinT*cost*costd - cosT*sint*sintd + cosT*cost*sintd - sinT*sint*sintd

ar = cosT*cost*costr + sinT*sint*costr
br = cosT*sint*sintr - sinT*cost*costr
gr = sinT*cost*costr - cosT*sint*sintr + cosT*cost*sintr - sinT*sint*sintr

#print ad.shape, ar.shape, gd.shape, gr.shape
first = 1/(2*w)


# calculations
part1 = (first*((ad)*(w*T - (np.sin(2*w*T))/2))) + (first*((ar)*(w*T - (np.sin(2*w*T))/2)))
part2 = first*((bd+br)*(w*T + (np.sin(2*w*T))/2))
part3 = first*((gd+gr)*sinT*sinT)

'''
plt.plot(ad, label='ad')
plt.plot(ar, label='ar')
plt.legend()
plt.show()
plt.plot(bd, label='bd')
plt.plot(br, label='br')
plt.legend()
plt.show()
plt.plot(gd, label='gd')
plt.plot(gr, label='gr')
plt.legend()
plt.show()
plt.plot(part1, label = 'part1')
plt.plot(part2, label = 'part2')
plt.plot(part3, label = 'part3')
plt.legend()
plt.show()
'''
#z_calc = (part1)
z_calc = (part1 + part2 + part3)
plt.plot(z_calc, label='calculated')
plt.legend()
plt.show()


