import matplotlib.pyplot as plt
import numpy as np



# Uppgift 1 _______________________________________________________________________________________

# Vi vill minimera |Y-AX| 

# funktion som givet punkter i planet (aj, bj) 
# så "alla_punkter_array" är en np.array
def uppgift1(alla_punkter_array):

    # skapar A matrisen
    # 1. först hämtar vi alla a värden som de är (kolumn 3)
    a = alla_punkter_array[ :, 0] # alla rader, och endast första kolumnen
    # 2. skapa de 3 andra kolumnerna
    # nu skapar vi hela A matrisen genom kolumnerna
    A = np.column_stack((a**3, a**2, a, np.ones_like(a)))

    # skapar Y matrisen genom att ta alla y-punkter från arrayen av punkter, 
    # det är bara den alla rader och endast den andra kolumnen
    y = alla_punkter_array[ :, 1]
    Y = np.vstack(y) # stackar alla y värden i en kolumn

    # Beräknar X ur normalekvationen nedan nu efter A och Y matriserna är skapade
    # normalekvationen: A^T(AX) = A^T(Y)
        # då A^T(A) är inverterbar fås  X = (((A^T)(A))^-1)(A^T)Y
    # Transponat av A:
    A_trans = A.T
    A_trans_A = np.matmul(A_trans,A)
    inv_A_trans_A = np.linalg.inv(A_trans_A)
    A_plus = np.matmul(inv_A_trans_A, A_trans) # A_plus är pseudoinversen
    X = np.matmul(A_plus, Y)
            
    return X


# Uppgift 2 _______________________________________________________
test_array1 = np.zeros((8,2))  # skapar nu en array av 8 värden där varje värde har två värden
for i in range(0,8):     # {[0,0],[0,0],[0,0], ...}  
        test_array1[i,0] = np.random.rand()*2 +1    # för att skapa värdena 1-3, istället för 0-1
        test_array1[i, 1] = np.random.rand()*2 +1   

# gör om arrayen med de godtyckliga punkterna
test_array1_np = np.array(test_array1)
test1 = uppgift1(test_array1_np) # använder minsta kvadratmetoden för att skapa grad 3 polynom
p3 = test1[0]   # sparar varje X kolumn värde i grad 3 polynomet
p2 = test1[1]
p1 = test1[2]
p0 = test1[3]

polynom_x_values = np.linspace(0,3,100)  # skapar fördelningen mellan 0 och 3 av 100 jämna delningar
polynom_y_values = p3*(polynom_x_values**3) + p2*(polynom_x_values**2) + p1*polynom_x_values + p0  # y värdena från grad 3 polynomet


# plottar först alla 8 godtyckliga punkter 
plt.scatter(test_array1[:,0], test_array1[:,1], marker='o',color="purple")
plt.plot(polynom_x_values,polynom_y_values) # plottar approximationen av punkterna
plt.show()





























