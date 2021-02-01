teikums = (input("ievadiet īsu teikumu- "))
print(f"teikumā ir {len(teikums)} simboli")

pirmaisBurts = (input("ievadiet vārdu- "))
print(pirmaisBurts[0]) 

teksts = "Sveika, Pasaule!"
print(teksts[10:15])

teikums2 = (input("ievadiet īsu teikumu- "))
print(teikums2.upper())

teikums3 = (input("ievadiet īsu teikumu- "))
print(teikums3.lower())


vards = "samērcēt"      
pedejieBurti = vards[1:]
print("p" + pedejieBurti)

print(teksts.strip())

#Izveido programmu, kas lietotājam pajautā ievadīt teikumu un izdrukā to, kad katra vārda pirmais burts ir lielais.
teikums4 = (input("ievadiet īsu teikumu- "))
print(teikums4.title())

vards = (input("ievadiet savu vārdu- "))
print(f"{vards[::-1].title()}. Pamatīgs juceklis, vai ne, {vards[0]}?")


