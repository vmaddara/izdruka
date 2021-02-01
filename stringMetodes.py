#Man -> Gan
vards = "Māja"       #0000
ped_burti = vards[1:]
print("G" + ped_burti)

#string konkatinācija
x = "Sveika, pasaule, "
x = x + "tu esi skaista!"

print(x)
print(2 + 3)
print("2" + "3")  #nedrīks saskaitīt string ar skaitļiem

print(x.upper())  #izdrukā tikai ar lielajiem burtiem
print(x.lower())  #izdrukā tikai ar mazajiem burtiem
print(x.split())  #sadala pa vārdiem
print(x.split("a")) #sadala elementos pēc a
print(x.())