#iterācija - kādas darbības atkārtota izpildīšana
mainigais = [1, 2, 3]
for elements in mainigais:
    print(elements)  #darbības, kas jāveic

#drukā list elementus
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for sk in myList:
    print(sk)

for _ in myList:
    print("Sveiki!")  #var nerakstīt cikla mainīgā nosaukumu

#izdrukā tikai pāra skaitļus
for sk in myList:
    if sk % 2 == 0:
        print(sk)
    else:
        print(f"{sk} ir nepāra skaitlis")

#--------------------
#SUMMAS APRĒĶINĀŠANA
#--------------------
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
summa = 0

for sk in myList:
    summa = summa + sk
    print(f"Pēc {sk} skaitļu saskaitīšanas ir {summa}")
print(summa)

#drukā ar tekstu
myString = "Sveika, pasaule!"
for burts in myString:
    print(burts)

for burts in "programma":
    print(burts, end=" ")

#drukā tuple
tup = (1, 2, 3, 4)
for elements in tup:
    print(elements)

myList = [(1, 2), (3, 4), (5, 6), (7, 8)] #packed tuple
print(len(myList))

for elements in myList:
    print(elements)

for (a,b) in myList: #atpako tuple
    print(a)

for viens,otrs in myList: #var nelikt iekavas
    print(viens)
    print(otrs)

myList=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in myList:
    print(b)

#vārdnīcas
d = {"k1":11, "k2":12, "k3":13}
for elements in d: 
    print(elements) #izdrukā tikai atslēgas

for elements in d.items(): 
    print(elements) #drukā pārus

for key,vertiba in d.items(): 
    print(vertiba)

#ar skaitļiem izmanto funciju range()

for skaitlis in range(15): #izdrukā visus skaitļus no [0:15)
    print(skaitlis)

for skaitlis in range(5, 15):#izdrukā visus skaitļus no [5:15)
    print(skaitlis)

for skaitlis in range(5,15,2):#izdrukā visus skaitļus no [5:15) ar soli 2
    print(skaitlis)

N=int(input("Ievadi skaitli: "))
for sk in range(1, N+1):
    print(sk)
    