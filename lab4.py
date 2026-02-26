import numpy as np
from scipy import linalg as LA
from sympy import Matrix 
import time


#  Uppgift 1.1 __________________________________________
A_test = Matrix([[1,2,1,-1,2],[3,4,5,2,0],[2,2,1,0,2]])  # här skapar vi den färdiga A matrisen i uppgiften
X_test, pivot_test = A_test.rref()    # vi löser 
X_test_sista_kolumn = X_test[:,-1]
print(X_test_sista_kolumn)


#  Uppgift 1 __________________________________________
# först bildar vi en 100x100-matris A med slumptal genom sympy Matrix
A_1 = Matrix(np.random.rand(100,100)) 

# sedan bildar vi en 100-vektor y med slumpal genom sympy Matrix
Y_1 = Matrix(np.vstack(np.random.rand(100)))

# vi använder rref() för att lösa Ax=y
t_start=time.time()  # variabel som håller start tiden
X_whole,pivots = A_1.row_join(Y_1).rref() # utför beräkningen av AX=Y
t_end = time.time()
# vi beräknar tiden det tar för att lösa Ax=y
print("Time taken for floats: ", t_end-t_start)  # för rref() med random.rand tar det ca. 15s




# Nu testar vi samma metod fast med np.random.randint() istället för np.random.rand()

# using random.randint ()  heltal från 0-7 väljer vi slumpmässigt
A_2 = Matrix(np.random.randint(1,7,(100,100)))

# sedan bildar vi en 100-vektor y med slumpal genom sympy Matrix
Y_2 = Matrix(np.vstack(np.random.randint(1,7,(100))))


t_start2=time.time()  
X2_whole,pivots = A_2.row_join(Y_2).rref() # utför beräkningen av AX=Y
t_end2 = time.time()
# vi beräknar tiden det tar för att lösa Ax=y
print("Time taken for int: ", t_end2-t_start2)  # för rref() med random.randint tar det ca. 0.3s, alltså mycket snabbare än random.rand()


# här sparar vi X värdena i variabler som vi använder i epsilon beräkningarna för att se om skilladen är korrekt
X_1 = X_whole[:,-1]
X_2 = X2_whole[:,-1]



# Vi verifiera att lösningen är korrekt, vi gör detta genom att använda epsilon
# och jämföra våra värdens skillnad med de korrekta
epsilon = 1e-9
diff_1 = A_1*X_1 - Y_1  # beräknar skillnaden mellan den riktiga Y-matrisen och våran egna beräkande Y-matris
my_solution = True # vi antar att vår lösning är korrekt inom numerisk tolerans (epsilon)
for i in diff_1:
    if abs(i) >= epsilon:  # om något element i vår lista av skillader mellan de två Y-matriserna skiljer sig mer än epsilon,
        my_solution = False  # så är svaret felaktigt
        break

print("Beräkningen för random.rand är: ", my_solution)

epsilon2 = 1e-9
diff_2 = A_2*X_2 -Y_2
my_solution2 = True
for i in diff_2:
    if abs(i) >= epsilon2:
        my_solution2 = False
        break
print("Beräkningen för random.randint är: ", my_solution2)






#  Uppgift 2 __________________________________________

time_float_upg2_start = time.time()  #tiden startar

# först gör vi om alla arrays till decimalform så att de kan inversera senare
A_1_np = np.array(A_1).astype(float)
A_1_inv = LA.inv(A_1_np)  # för float elementen
Y_1_float = np.array(Y_1).astype(float)

X_upg2_float = np.matmul(A_1_inv,Y_1_float)  # här beräknar vi X matrisen för random.rand()
  
time_float_upg2_end = time.time()  #tiden slutar





# för floats
time_int_upg2_start = time.time() #tiden startar

A_2_np = np.array(A_2).astype(float)
A_2_inv = LA.inv(A_2_np)  # för int elementen
Y_2_int = np.array(Y_2).astype(float)

X_upg2_int = np.matmul(A_2_inv, Y_2_int)  # här beräknar vi X matrisen för random.randint()

time_int_upg2_end = time.time()  #tiden slutar




# vi printar ut skillnaden i tiden 
print("Time taken for upgift 2 floats: ", time_float_upg2_end-time_float_upg2_start)  # tiden för random.rand() tar ungefär 0.03 s
print("Time taken for uppgift 2 ints: ", time_int_upg2_end-time_int_upg2_start)  # tiden för random.randint() tar ungefär 0.02s

# Slutsats: vi kan alltså se att använda invers för A för att beräkna ut X är snabbare än att använda rref().




# vi kollar också om skilladen för svaret är rätt genom epsilon igen
epsilon = 1e-9
diff_upg2_float = A_1_np*X_1 - Y_1_float  # beräknar skillnaden mellan den riktiga Y-matrisen och våran egna beräkande Y-matris
my_solution_upg2_float = True # vi antar att vår lösning är korrekt inom numerisk tolerans (epsilon)
for i in diff_upg2_float:
    if abs(i) >= epsilon:  # om något element i vår lista av skillader mellan de två Y-matriserna skiljer sig mer än epsilon,
        my_solution_upg2_float = False  # så är svaret felaktigt
        break
print("Beräkningen för random.rand  uppgift 2 är: ", my_solution_upg2_float)

epsilon2 = 1e-9
diff_upg2_int = A_2_np*X_2 -Y_2_int  # 
my_solution2_upg2_int = True
for i in diff_upg2_int:
    if abs(i) >= epsilon2:
        my_solution2_upg2_int = False
        break
print("Beräkningen för random.randint uppgift 2 är: ", my_solution2_upg2_int)





