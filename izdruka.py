"""Komentārus var rakstīt
vairākās
rindās"""
print("HELLO WORLD")
print(2 * 2)
print(2 * 2, 2 * 3, 2 * 4, "pitons")
print(f"Ja saskaitīsim 5 ar 7 iegūsim {5+7}.") #kombinētā izdruka
print("Sveika, "+"pasaule!")
print("Madara "*5)
print(365*24*60*60)
print(0.1 + 0.2 - 0.3)
print()
print()

#mainīgie
a = 5
print(a)
print(a + a)
a = a + a + a#Ar = piešķir vērtību
print(a)
print(type(a))  #int-veselie skaitļi
a = 30.1
print(type(a))  #float-decimāldaļa

#nodokļi
mani_ienakumi = 367
nodoklis = 0.2 #tas ir 10%
maniNodokli = mani_ienakumi * nodoklis
print(maniNodokli)

#datu ievade
x = input("Ievadi vārdu: ")
print("Tavs ievadītais vārds ir " + x)