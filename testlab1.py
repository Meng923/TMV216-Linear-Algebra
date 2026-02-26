import matplotlib.pyplot as plt
import numpy as np

P = np.array([0,0,1])
Q = np.array([1,0,1])
R = np.array([0,1,1])

cross_product = np.cross(Q-P, R-P)
norm_v = cross_product / np.linalg.norm(cross_product)

mittpunkt = (P + Q + R) / 3

fig = plt.figure()
ax2 = fig.add_subplot(111, projection='3d')

ax2.scatter(
    mittpunkt[0], mittpunkt[1], mittpunkt[2],
    color="blue", s=100
)

ax2.set_xlim(-1, 2)
ax2.set_ylim(-1, 2)
ax2.set_zlim(0, 3)

plt.show()
















P = np.array([0, 0, 1])  # e.g P:(0,0,1)
Q = np.array([1, 0, 1])   # e.g  Q:(1,0,1)
R = np.array([0, 1, 1])   # R:(0,1,1)

# Del 2.2 __________________________________________________________________________
# plotta upp trianglen med hörn i våra hardkodade punkter P, Q, R
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection="3d")

# kopierar våra punkter i nya variabler för att kunna sluta den sista punkten
x_values = [P[0], Q[0], R[1], P[0]] 
y_values= [P[1], Q[1], R[1], P[1]] 
z_values = [P[2], Q[2], R[2], P[2]]

# här plottar vi triangel med punkterna och drar linjer mellan dem
ax2.plot3D(x_values, y_values, z_values, "-o", color="purple")


#plt.show()



# Del 2.3 ______________________________________________________________

# Våran startpunkt är punkt P, som vi satte förut till P:(0,0,1)
# Våra två riktningsvektorer kommer vara PQ och PR (se rad 105)

# planet skall skrivas i parameterform:
# Då vi redan har hardkodad våra punkter till att vara:
#      P:(0,0,1)
#      Q:(1,0,1)
#      R:(0,1,1)

#    Riktningsvektor PQ: blir då Q-P = (1,0,0)
#    Riktningsvektor PR: blir då R-P = (0,1,0)

# Alltså är vår parameterekvation:
#                                  x = s
#                                  y = t  ,   s,t tillhör Reella tal
#                                  z = 1 



# Del 2.4_____________________________________________________________
# beräknar  normalvektorn: 
norm_v = cross_product / np.linalg.norm(cross_product)  

#beräknar mittpunkten
mittpunkt = (P+Q+R)/3   # detta är samma som (1/3)*((0,0,1)+(1,0,1)+(0,1,1))
ax2.quiver(*mittpunkt, *norm_v, color="blue") # plottar normalvektorn med start i mittpunkt

ax2.set_xlim(-0.5, 1.5)
ax2.set_ylim(-0.5, 1.5)
ax2.set_zlim(0, 2)
ax2.view_init(25, 45)
plt.show()

print("cross_product:", cross_product)
print("norm_v:", norm_v)
print("mittpunkt:", mittpunkt)