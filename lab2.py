import matplotlib.pyplot as plt
import numpy as np


# Uppgift 1 ____________________________________________________________

lst_vectors1 = []  # skapar en tom lista ska innehålla alla genererade vektorer

# funktion som tar parametrarna: 2x2 matrix A, vektor v0, och ett positivt heltal n
def uppgift1(A, v0, n):

    if n<= 0: # om heltalet har rekursivt nått n<=0, dåhar vi generert klart alla vektorer och returnerar då listan av dem
        return np.array(lst_vectors1) # gör om listan till en np.array lista
    else: 
        current_vector1 = v0  # vi sätter en ny variabel till det nuvarande v0 vektorn
        new_vector1 = np.matmul(A,current_vector1)  # utifrån formeln beräknar vi multiplicerar matriserna via np.matmul
        lst_vectors1.append(new_vector1) # lägger till den nya beräknade vektorn till vår tidigare lista av vektorer

        # här sker rekursionen där vi samtidigt gör om listan till en np.array lista
        # vi kallar på funktionen igen, men sätter in den nya vektor, samt minskar heltalet n med 1
        return np.array(uppgift1(A, new_vector1, n-1)) 
    


# testar vår funktion med en godtycklig matris
A = np.array([ [1,2], [2,4] ])  # sätter 2x2 matrisen till en np-array
v0 = np.array([7,2])  # skapar en startvektor som är godtycklig
n = 5 # väljer ett godtyckligt heltal n
print(uppgift1(A,v0,n)) # printar ut resultatet för att se om funktionen fungerar korrekt








# Uppgift 2 ____________________________________________________________

# Skriver ner alla A matriser till variabeln vid namn A_i, alltså innehåller A2: A1, A2, A3, A4 given i frågan
A_i = np.array([[[0,0],[0, 0.16]], [[0.85, -0.05 ],[ 0.05, 0.85]], 
               [[0.2 , -0.26],[0.23, 0.22]], [[-0.15, 0.26],[ 0.28, 0.24]]])

# Skriver ner alla b vektorer till en varibel vid namn b_i: b1, b2, b3, b4
b_i = np.array([[0,0],[0, 1.6],[0, 1.2],[0, 0.44]])

# skapar en variabel lista som ska innehålla alla punkter i koordinatsystemet
lst_vectors2 = []

# en funktionen som tar in matriserna A_i, vektorerna b_i, en startvektor v02, samt ett heltal n
def uppgift2(A_i,b_i,v02,n):
     
    r2= np.random.rand()  # genererar ett godtyckligt tal mellan 0 och 1

    if r2>0.93:  # först om det godtyckliga talet är 
        current_A = A_i[3]  # väljer matris A4
        current_b = b_i[3]  # väljer vektor b4
    elif r2>0.86:
        current_A = A_i[2]  # väljer matris A3
        current_b = b_i[2]   # väljer vektor b3
    elif r2>0.04:
        current_A = A_i[1]  # väljer matris A2
        current_b = b_i[1]   # väljer vektor b2
    else:
        current_A = A_i[0]   # väljer matris A1
        current_b = b_i[0]   # väljer vektor b1


    if n<=0:  # kollar om heltalet nu har blivit mindre eller lika med 0 efter rekursionen
        return np.array(lst_vectors2)  # returnerar listan av de nya genererade vektorn 
    else:
        current_vector2 = v02  # sätter en variabel som håller koll på det nuvarande vektor parametern
        new_vector2 = np.matmul(current_A, current_vector2) + current_b  #utför beräkning baserad på formeln i frågan
        lst_vectors2.append(new_vector2)  #lägger till den nya genererade vektorn till vår vektor lista

        return np.array(uppgift2(A_i,b_i,new_vector2,n-1))  # här sker rekursionen där ni nu sätter in den nya vektor parametern och minsar heltalet med 1


# nedan testar vi med godtyckliga parametrar för att få fram bilden i koordinatsystemet
v02 = np.array([1,2])
n = 995

# vi kallar på funktionen och sparar den genererade listan av alla vektorer som nu då är punkter till variabeln all_vectors
all_vectors = uppgift2(A_i,b_i,v02,n)
     
x = all_vectors[:,0] # vi vill spara alla x-koordinator från alla vektorer
y = all_vectors[:,1]  # här sparar vi alla y-koordinator från vektorerna

plt.subplot(121)   
plt.plot(x,y,'o', color="purple")  # plottar upp koordinatsystemet 
plt.axis([-5,4,-1,11]) # sätter axlarna så att vi kan se tydligt

plt.show()

