import matplotlib.pyplot as plt
import numpy as np




# Uppgift 1 ____________________________________________________________

lst_vectors1 = []  # skapar en tom lista ska innehålla alla nya vektorer

# funktion som tar parametrar 2x2 matrix, 2-vektor och ett positivt heltal n
def uppgift1(A, v0, n):

    if n<= 0:
        return np.array(lst_vectors1)
    else:
        current_vector1 = v0
        new_vector1 = np.matmul(A,current_vector1)
        lst_vectors1.append(new_vector1)

        return np.array(uppgift1(A, new_vector1, n-1))
    
# testing our function with random numbers
A = np.array([ [1,2], [2,4] ])  # omvandlar 2x2 matrisen till en np-array

v0 = np.array([7,2])
n = 5

print(uppgift1(A,v0,n))


'''
        genererar en ny vektor vk = A * v(k-1)

        we first have v0 as a parameter


        v1 = A*v0

        v2 = A*v1

        v3 = A*v2

        ...

        vn = A*v(n-1)



    '''







# Uppgift 2 ____________________________________________________________

A2 = np.array([[[0,0],[0, 0.16]], [[0.85, -0.05 ],[ 0.05, 0.85]], [[0.2 , -0.26],[0.23, 0.22]], [[-0.15, 0.26],[ 0.28, 0.24]]])
b2 = np.array([[0,0],[0, 1.6],[0, 1.2],[0, 0.44]])
percentages = [0.04,0.82,0.07,0.07]



lst_vectors2 = []

def uppgift2(A2,b2,v02,n):
     
    r2= np.random.rand()   # e.g 0.723

    if r2>0.93:
        current_A = A2[3]
        current_b = b2[3]
    elif r2>0.86:
        current_A = A2[2]
        current_b = b2[2]
    elif r2>0.04:
        current_A = A2[1]
        current_b = b2[1]
    else:
        current_A = A2[0]
        current_b = b2[0]


    if n<=0:
        return np.array(lst_vectors2)
    else:
        current_vector2 = v02
        new_vector2 = np.matmul(current_A, current_vector2) + current_b
        lst_vectors2.append(new_vector2)

        return np.array(uppgift2(A2,b2,new_vector2,n-1))


v02 = np.array([1,2])
n = 995

all_vectors = uppgift2(A2,b2,v02,n)
     
print(uppgift2(A2,b2,v02,n))
x = all_vectors[:,0]
y = all_vectors[:,1]

plt.subplot(121)
plt.plot(x,y,'o', color="purple")
plt.axis([-4,3,0,10])




plt.show()





























