import matplotlib as plt
import numpy as np

# Lab 1


# Question 1 _________________________________________________
P = np.array([1,1,1])
plane1 = np.array([1,2,2])   # normalriktning för plan 1
plane2 = np.array([-1,3,-1])  # normalvektorn för plan 2





def f(P):

    # vi räknar ut OS 
    u_prime = ( (np.dot(P, plane1)) / (abs(np.dot(plane1,plane1))) ) * plane2

    return u_prime


print(f(P))













