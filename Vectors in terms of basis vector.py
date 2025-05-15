from math import sqrt
import numpy as np
from tkinter import *
from tkinter import messagebox 

#Take the 2 dimensional vector as input from the user 

v = np.array([[2],
             [3]])

#Ask the user which basis he would like to get the output in 
basis_msg = u"Input numbers according to your choise of base\n" \
"1. |\u2191> and |\u2193> \n" \
"2. |\u2192> and |\u2190> \n" \
"3. |\u2197> and |\u2199>"

messagebox.showinfo("Which Basis vector?", basis_msg)
choice = int(input("Enter your choice (1,2,3)"))

b1 = b2 = [0,0]

if choice == 1:     #standard basis
    b1 = np.array([1, 0])   #|↑>
    b2 = np.array([0, 1])   #|↓>
elif choice == 2:
    b1 = np.array([1/sqrt(2), -1/sqrt(2)])     #|→>
    b2 = np.array([1/sqrt(2), 1/sqrt(2)])      #|←>
elif choice == 3:
    b1 = np.array([1/2, -sqrt(3)/2])     #|↗>
    b2 = np.array([sqrt(3)/2, 1/2])      #|↙>   
else: 
    messagebox.showerror("Error", "Invalid input")


def GetCoeff(b1,b2):
    x1 = b1@v
    x2 = b2@v
    print("The compoenents are ", x1, x2)
    return x1,x2



GetCoeff(b1,b2)

