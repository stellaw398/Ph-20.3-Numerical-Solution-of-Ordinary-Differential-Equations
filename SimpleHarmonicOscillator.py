#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:21:32 2018

@author: apple
"""
import matplotlib.pyplot as plt
import numpy as np
N = 200
t=0
x_olde=5
v_olde=.5
x_oldi = x_olde
v_oldi = v_olde
h= .1
det = 1/(1 + (h)**2)
for i in range(0,N+1): 
    t_new = t + h*i
    X= 5*np.cos(t_new)
    V= -5*np.sin(t_new)
    x_newe = x_olde +(h*v_olde)
    x_newi = det*(x_oldi +(h*v_oldi))
    v_newe = v_olde -(h*x_olde)
    v_newi = det*(v_oldi-(h*x_oldi))
    Ee= (x_newe)**2 + (v_newe)**2
    Ei=(det*x_newi)**2 + (det*v_newi)**2
    #plt.plot(t_new,x_newe,'bo');plt.plot(t_newe, v_newe,'ro')#explicit
    #plt.plot(t_new,x_newi,'ko');plt.plot(t_new, v_newi, 'yo')#implicit
    #plt.plot(t_new,X-x_newe,'g^' );plt.plot(t_new,V-v_newe,'c^') #explicit error
    #plt.plot(t_new,X-x_newi,'kx' );plt.plot(t_new,V-v_newi,'mx')#implicit error
    #plt.plot(t_new,Ee, 'm>'); plt.plot(t_new,Ei,'b*')
    ##phase space
    plt.plot(x_newe, v_newe,'r<'); plt.plot(x_newi, v_newi, 'y>' ); plt.plot(X,V,'bo')
    x_olde = x_newe
    v_olde = v_newe
    x_oldi = x_newi
    v_oldi = v_newi
x_old=5
v_old=.5  
##symplectic Euler
for i in range(0,N+1):
    t_new = t + h*i
    x_new = x_old + h*v_old
    v_new = v_old - h*(x_new)
    X= 5*np.cos(t_new)
    V= -5*np.sin(t_new)
    E = (x_new)**2 + (v_new)**2
    plt.plot(x_new,v_new, 'g*')
    #plt.plot(t_new,E, 'bo')
    x_old = x_new
    v_old = v_new
plt.show()