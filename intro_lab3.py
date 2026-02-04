import numpy as np

'''

#______UPPGIFT 1_______________________________________
print("\n______UPPGIFT 1__________________________________\n")

A = np.array([[1,4,7,10],[2,5,8,11],[3,6,9,12]])
B = np.array([[1],[3],[5]])
C = np.array([[0,2,4,6,8]])

shape_a = A.shape    # shape gives you (rows, column)
shape_b = B.shape         # look at number 1 to knwo which vektor it is      
shape_c = C.shape

size_a = A.size    # size tells you the total nr of elements
size_b = B.size
size_c = C.size

min_A = A.min()   # min() and max() functions looks through every element
max_A = A.max()

type_A = A.dtype   # dtype = datatype and bits it takes?
type_B = B.dtype
type_C = C.dtype

print(shape_a)
print(shape_b)
print(shape_c)
print(size_a)
print(size_b)
print(size_c)

print(min_A)
print(max_A)

print(type_A)
print(type_B)
print(type_C)




#______UPPGIFT 2_______________________________________
print("\n______UPPGIFT 2__________________________________\n")



a = np.array([0,2,4])
b = np.array([1,3,5])
c = np.array([-1,0,9])
tre_d = np.dot(a,b)
tre_c = np.cross(a,b)
print(np.dot(tre_d,c))   # dot = multiplicerar vektorerna var för sig och summerar
print(np.cross(tre_c,c))


  #1. (dot)    ax(bxc) borde vara [0,0,180] =    180

        #är det samma som b(ac) - c(ab)

'''


#______UPPGIFT 3 _______________________________________
print("\n______UPPGIFT 3__________________________________\n")

A_org = np.array([[1,4,7,10],[2,5,8,11],[3,6,9,12]])
B_org = np.array([[4,5,6],[3,2,1],[1,1,1]])
C = np.array([[1],[3],[5]])
D = np.array([0,2,4])

A_new = A_org.copy()
B_new = B_org.copy()

# question a
for i in range(3):
    A_new[i][2] = C[i][0]
print(A_new)
print(A_org)


for i in range(3):
    B_new[1][i] = D[i]
print(B_new)
print(B_org)




#______UPPGIFT 4 _______________________________________
print("\n______UPPGIFT 4__________________________________\n")

'''
d = [2,3,7]
A1=np.diag(d,5)
A2=np.diag(d,1)
A3=np.diag(d,-1)

print(A1)

print()
print(A2)

print()
print(A3)


b1 = np.array([[4],[3],[1]])
b2 = np.array([[5],[2],[1]])
b3 = np.array([[6],[1],[1]])

B = np.hstack([b1,b2,b3])
print(B)
'''

#______UPPGIFT 5 _______________________________________
print("\n______UPPGIFT 5__________________________________\n")

A = np.array([[10,7,8,7],[7,5,6,5],[8,6,10,9],[7,5,9,10]])

A_part = np.array([[ A[1][1], A[1][2] ], [A[2][1] , A[2][2] ]])
print(A_part)





#______UPPGIFT 3 _______________________________________
print("\n______UPPGIFT 3__________________________________\n")




#______UPPGIFT 3 _______________________________________
print("\n______UPPGIFT 3__________________________________\n")






