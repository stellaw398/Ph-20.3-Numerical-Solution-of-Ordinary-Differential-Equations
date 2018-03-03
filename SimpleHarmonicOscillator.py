#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:21:32 2018

@author: apple
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import sys
N = float(sys.argv[1])#200
t=float(sys.argv[2])#0
x_olde=float(sys.argv[3])#5
v_olde=float(sys.argv[4])#.5
x_oldi = x_olde
v_oldi = v_olde
h= float(sys.argv[5])#.1
det = 1/(1 + (h)**2)
for j in range (5):
    h = h/(2**j)
    N = 200
    t=0
    x_olde=5
    v_olde=.5
    truncation=[]
    for i in range(N+1): 
        t_new = t + h*i
        X= 5*np.cos(t_new)
        V= -5*np.sin(t_new)
        x_newe = x_olde +(h*v_olde)
        x_newi = det*(x_oldi +(h*v_oldi))
        v_newe = v_olde -(h*x_olde)
        v_newi = det*(v_oldi-(h*x_oldi))
        Ee= (x_newe)**2 + (v_newe)**2
        Ei=(det*x_newi)**2 + (det*v_newi)**2
        E = X**2 + V**2
        if j == 0: #only plt for original h value
            plt.figure(0)
            plt.plot(t_new,x_newe,'bo');plt.plot(t_new, v_newe,'ro')#explicit
            plt.plot(t_new,x_newi,'ko');plt.plot(t_new, v_newi, 'yo')#implicit
            plt.figure(1)
            plt.plot(t_new,X-x_newe,'bo');plt.plot(t_new,V-v_newe,'ro') #explicit error
            plt.plot(t_new,X-x_newi,'ko');plt.plot(t_new,V-v_newi,'yo')#implicit error
            plt.figure(2)
            plt.plot(t_new,Ee, 'g*'); plt.plot(t_new,Ei,'r*'); plt.plot(t_new, E, 'ko')
            ##phase space
            plt.figure(3)
            plt.plot(x_newe, v_newe,'r<'); plt.plot(x_newi, v_newi, 'y>' ); plt.plot(X,V,'bo')
        truncation.append(abs(X-x_newe))
        x_olde = x_newe
        v_olde = v_newe
        x_oldi = x_newi
        v_oldi = v_newi
    maxerror=max(truncation)
    plt.figure(5)
    plt.plot(h, maxerror, 'bo')    
x_old=float(sys.argv[3])#5
v_old=float(sys.argv[4])#.5 
h= float(sys.argv[5])#.1 
##symplectic Euler
for i in range(0,N+1):
    t_new = t + h*i
    x_new = x_old + h*v_old
    v_new = v_old - h*(x_new)
    X= 5*np.cos(t_new)
    V= -5*np.sin(t_new)
    Es = (x_new)**2 + (v_new)**2
    plt.figure(3)
    plt.plot(x_new,v_new, 'g*')
    plt.figure(4)
    plt.plot(t_new,Es, 'bo')
    x_old = x_new
    v_old = v_new
plt.figure(0) ## Harmonic Oscillations of x and v for implicit and explicit
plt.xlabel('time')
blue_patch = mpatches.Patch(color='blue', label='x explicit euler');red_patch = mpatches.Patch(color='red', label='v explicit euler');black_patch = mpatches.Patch(color='black', label='x implicit euler');yellow_patch = mpatches.Patch(color='yellow', label='v implicit euler')
plt.legend(handles=[blue_patch, red_patch, black_patch, yellow_patch])
plt.savefig('HarmonicMotion.pdf')
plt.close()

plt.figure(1)##Global Error
plt.xlabel('time')
plt.ylabel('error')
blue_patch = mpatches.Patch(color='blue', label='x explicit euler error');red_patch = mpatches.Patch(color='red', label='v explicit euler error');black_patch = mpatches.Patch(color='black', label='x implicit euler error');yellow_patch = mpatches.Patch(color='yellow', label='v implicit euler error')
plt.legend(handles=[blue_patch, red_patch, black_patch, yellow_patch])
plt.savefig('Globalerror.pdf')
plt.close()

plt.figure(2)
plt.xlabel('time')
plt.ylabel('Energy')
green_patch = mpatches.Patch(color='green', label='Explicit Energy'); red_patch = mpatches.Patch(color='red', label='Implicit Energy'); black_patch = mpatches.Patch(color='black', label= 'Analytic Energy')
plt.legend(handles= [green_patch, red_patch, black_patch])
plt.savefig('Energy.pdf')
plt.close()

plt.figure(3)
plt.xlabel('X')
plt.ylabel('V')
red_patch = mpatches.Patch(color='red', label=' Explicit Euler'); yellow_patch = mpatches.Patch(color='yellow', label='Implicit Euler'); blue_patch = mpatches.Patch(color='blue', label='Analytic'); green_patch = mpatches.Patch(color='green', label='Symplectic Euler')
plt.legend(handles=[red_patch, yellow_patch, blue_patch, green_patch])
plt.savefig('PhaseSpace.pdf')
plt.close()

plt.figure(4)
plt.xlabel('time')
plt.ylabel('Energy')
blue_patch = mpatches.Patch(color='blue', label='Symplectic Energy')
plt.legend(handles= [blue_patch])
plt.savefig('EnergySym.pdf')
plt.close()

plt.figure(5)
plt.semilogy()
plt.semilogx()
plt.xlabel('h')
plt.ylabel('truncation error')
plt.savefig('truncationerror.pdf') 
plt.close
