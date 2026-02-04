import numpy as np
import matplotlib.pyplot as plt


# ____Uppgift 1_____________________________________________________________________-

'''  vektorn u = (3,4)
    normalvektorn = vinkelrät vektor alltså skalärprodukt av dem = 0
    3x + 4y = 0
    (x,y) = (t, (-3/4)*t )   

'''




'''
fig, ax=plt.subplots()

# linjen 3x-4y+2=0
def xt(t): 
    return [t,(4/3)*t + (1/2)]  # se ipad för beräkning av x och y uttryck i t
P=np.array([xt(-2), xt(2)])
ax.plot(P[: , 0], P[: , 1], color="pink", linewidth=3)

# vektor u r(t) = t(3t, 4t)
def x3t(t):
    return [3*t, 4*t]
P3 = np.array([x3t(-1), x3t(1)])
ax.plot(P3[: , 0], P3[: , 1], color="purple", linewidth=3)



# normalvektorn till vektorn u
def x2t(t):
    return [t, (-3/4)*t]
P2=np.array([x2t(-2), x2t(2)])
ax.plot(P2[: , 0], P2[: , 1], color="red", linewidth=3)
# ax.quiver(0, 0.5, 3, -4, angles="xy", scale_units="xy", scale=5) vektor som pil



ax.axis('equal')
ax.grid('on')
plt.show()

'''




# ____Uppgift 2_________________________________________

'''
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection="3d")

def l1(x,y): 
    return 1 - 2*x + 2*y
x = np.linspace(-1,1,10)
y = np.linspace(-1,1,10)
X, Y = np.meshgrid(x,y)
ax2.plot_surface(X,Y, l1(X,Y), color="blue", alpha=0.5)

ax2.view_init(15,-115)
ax2.set_box_aspect((1,1,1))
ax2.set_xticks([-1,0,1])
ax2.set_yticks([-1,0,1])
ax2.set_zticks([-4,-2,0,2,4])



#linjen i planet vi kallar den r1
def xt22(t):
    return [-0.5 + 0.5*t, -1+t, t]
P = np.array([xt22(0), xt22(2)])
ax2.plot3D(P[: , 0], P[: , 1], P[: , 2], color="red", linewidth=3)



# normalvektorn till linjen r1
P2 = np.array([[0,0,1],[2,-2,1]])
ax2.plot3D(P2[: , 0], P2[: , 1], P2[: , 2], color="pink", linewidth=3)


plt.show()
'''


# ____Uppgift 3_________________________________________


fig3 = plt.figure()
ax3 = fig3.add_subplot(projection="3d")

P = np.array([0.1, 0.2, 0.3])
Q = np.array([0.8, 0.1, -0.1])
R = np.array([0.9, 0.7, 0.4])



x = np.linspace(0,1,20)
y = np.linspace(0,1,20)
X, Y = np.meshgrid(x,y)

# the coordinates calculated from myself 
Xx = 0.1 + 0.7*X + 0.8*Y
Yy = 0.2 - 0.1*X + 0.5*Y
Zz = 0.3 - 0.4*X + 0.1*Y

ax3.plot_surface(Xx,Yy,Zz, color="purple", alpha=0.5)

# the view
ax3.view_init(15, -45)
ax3.set_box_aspect((1,1,1))
"""
ax3.set_xticks([-1,0,1])
ax3.set_yticks([-1,0,1])
ax3.set_zticks([-1,0,1])
"""

# visar de tre punkterna
ax3.scatter(*P)
ax3.scatter(*Q)
ax3.scatter(*R)


plt.show()














