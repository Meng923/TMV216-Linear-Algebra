import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.art3d as mpl

# Lab 1


# Fråga 1 Beräkningen av spegelpunkten  ____________________________________________________________________
P = np.array([1,1,1])   # punkten i fråga
plan1 = np.array([1,2,2])   # normalriktning för plan 1
plan2 = np.array([-1,3,-1])  # normalriktning för plan 2

def f(P):
    # Steg 1: hitta normalriktingen för första planet: det har vi redan (plan1)

    # vi räknar ut vektor OP
    # Steg 2: då starten är O = origo = (0,0,0) kommer nu u=OP vektorn bli just P själv = (1,1,1)
    
    # Steg 3: Beräkna q = QP vektorn (den som är halvvägs mellan P och spegelbilden av P)
    # Detta gör vi via projektionsformeln
    q1 = ((np.dot(P,plan1))/((np.linalg.norm(plan1))**2))*(plan1)  # den första delen

    # Steg 4: beräkna nu självaste spegelbilden S som då är u-2*q
    s1 = P - 2*q1
    
    # Steg 5: speglar den nya punkten med nästa plan (plan2)
    q2 = ((np.dot(s1,plan2))/((np.linalg.norm(plan2))**2))*(plan2)

    s2 = s1 - 2*q2  # beräknar den andra reflektionen i planet

    return s2



# Ritar upp uppgift 1 _______________________________________________________________________________

# skapar en diagram att rita upp
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection="3d")

list_of_dots = []  # initierar en tom lista av punkterna vi vill rita upp
dot_to_plot = P   # punkten som skall ritas upp 

n = [5,20,100]     # antal gånger punkter skall ritas
colors = ["purple", "pink", "green"]   # en lista av olika färger för punkterna

# en for loop som går igenom de tre n värdena och väljer respektive, samt olika färger 
for i in range(3):  
    times = n[i]
    col = colors[i]

    # en for loop som tar antalet n - funktionen i nuvarande loopen och lägger till den till listan av punkter som skall ritas upp
    for j in range(times):
        dot_to_plot = f(dot_to_plot)  # utför beräkningen av den dubbla spegelbilden
        list_of_dots.append(dot_to_plot)  # den dubblade spegelbilden läggs i listan av punkter som skall ritas upp

    l_dots = np.array(list_of_dots)  # gör om listan till np-arraylista för enkel plottning

    ax1.plot(l_dots[ :, 0], l_dots[ :, 1], l_dots[ :, 2], c=col, marker="o" )  # plottar alla x,y,z värden för alla speglingar


ax1.view_init(15,-45)  # sätter en initial vinkelvy
plt.show()










# Uppgift 2 _______________________________________________________________________________________________________________

# gör om punkterna till np array list,   vi hårdkodar P, Q, R värden enligt följande:
P = np.array([0, 0, 1])  # P:(0,0,1)
Q = np.array([1, 0, 1])   # Q:(1,0,1)
R = np.array([0, 1, 1])   # R:(0,1,1)

# detta är vår lista av våra punkter P, Q, R
dot = [P,Q,R]
l_dots2 = np.array(dot)  # gör om listan till np-array list



# Del 2.1 __________________________________________________________________________
  # vi vill kolla om  a=b=c= 0
  #  om de är det = linjärt oberoende = ligger inte på samma linje --> ge felmedelande

   # Vi sätter P som startpunk
   # Vi vill nu beräkna riktingsvektorn PQ, 
PQ = Q-P   # då redan punkterna P och Q är en np.array görs subtractionen automatiskt
PR = R-P  # och sedan också PR


  # PQ*t = PR om det finns ett t som får PQ att bli PR, då är de på samma linje
cross_product = np.cross(PQ, PR)  # beräknar krossproudkten, alltså om de är på samma linje ifall krossprodukten är = 0

# kollar om de tre punkterna ligger i samma linje genom np.cross()
if np.all(cross_product== 0):  
    print("Punkterna ligger på samma linje")
else:  # våra hardkodade P, Q, R punkter ligger inte på samma linje
    print("Punkterna ligger inte på samma linje")  # ger felmeddelande om de inte ligger på samma linje




# Del 2.2 __________________________________________________________________________
# plotta upp trianglen med hörn i våra hardkodade punkter P, Q, R
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection="3d")

# sätter våra punkter i nya variabler för att kunna sluta den sista punkten
x_values = [P[0], Q[0], R[0], P[0]] 
y_values= [P[1], Q[1], R[1], P[1]] 
z_values = [P[2], Q[2], R[2], P[2]]

# här plottar vi triangel med punkterna och drar linjer mellan dem
ax2.plot3D(x_values, y_values, z_values, "-o", color="purple")


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
# beräknar normalizerad normalvektorn (så längden är 1 ): 
norm_v = cross_product / np.linalg.norm(cross_product)  

#beräknar mittpunkten via given formel
mittpunkt = (P+Q+R)/3   
ax2.quiver(*mittpunkt, *norm_v, color="blue", length=1, linewidth=2) # plottar normalvektorn med start i mittpunkt

# plottar mittpunkten
ax2.scatter(mittpunkt[0], mittpunkt[1],mittpunkt[2], color="purple", s=30)

# sätter x,y,z axlar så triangel syns tydligt
ax2.set_xlim(-1, 2)
ax2.set_ylim(-1, 2)
ax2.set_zlim(0, 3)
ax2.view_init(25,45)
plt.show()


