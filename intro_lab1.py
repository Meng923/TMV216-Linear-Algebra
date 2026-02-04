import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve




#___UPPGIFT 1____done___________________________________
r = 4
a = np.pi*r**2

print(round(a))

#___UPPGIFT 2______done_________________________________
x = np.arange(0, 4*np.pi, 0.1)
#x = np.arange(5, 4*np.pi, 3)   
f = x*np.sin(x) 

plt.plot(x,f) 
plt.show()



'''
arannge(0, 10, 2)  = range()  values=(0,2,4,6,8)

linspace(0, 10, 2) = values(0,10)
linspace(0, 10, 3) = values()
'''



#___UPPGIFT 3_____done__________________________________


#___UPPGIFT 4_______________________________________
real = np.pi/4
s = 0
for i in range(100):
    s = s + ( ((-1)**i)/(2*i+1) )      # s= 0.78203840385
        #         s = 0
        # i=0    s = 0 + (1/1) = 1 
        # i=1     s = 1 + (-1/3) = 1 -(1/3)
        # i=2      s = 1-(1/3) + (1/5)


s2 = 0
for i in range(50):
    s2 = s2 + ( ((-1)**i)/(2*i+1) )

s3 = 0
for i in range(2):
    s3 = s3 + ( ((-1)**i)/(2*i+1) )


# testing our values
print("real:", real)       # answer: 2 decimals correct: 0.78
print("task:", s)
print("test range 50:", s2)
print("test range 2:", s3)
print(np.pi)





#___UPPGIFT 5_______________________________________
print("_________________________")

sn=0
n=0
t1 = abs(4*sn - np.pi)    # t1 = 3.14
t2 = (1/2) * 10**(-5)    

while (t1>t2):
    sn += ( ((-1)**n)/(2*n+1) )
    n +=1
    t1 = abs(4*sn - np.pi)

print(n)




#___UPPGIFT 6_______________________________________

def min_fun(x):
    y = (x**2) - np.cos(x)
    return y

x = np.linspace(-1.5, 1.5)  
y = min_fun(x)


z = fsolve(min_fun, 1)
w = fsolve(min_fun, -1)

plt.plot(x,y)
plt.plot(z, min_fun(z), 'o')
plt.plot(w, min_fun(w), 'o')
plt.grid('on')
plt.show()
