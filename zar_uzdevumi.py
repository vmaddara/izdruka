#uzdevums 1
"""
a=15.0
b=2.5
c=4.78
if a>b and a>c:
    print(f"skaitlis {a} ir vislielākais")

elif b>a and b>c: 
   print(f"skaitlis {b} ir vislielākais")

else: 
    print(f"skaitlis {c} ir vislielākais")
if a<b and a<c:
    print(f"skaitlis {a} ir mazākais")

elif b<a and b<c: 
   print(f"skaitlis {b} ir mazākais")

else: 
    print(f"skaitlis {c} ir mazākais")

#-------------------------------------------------------
#uzdevums 2
temp=float(input("Kāda ir jūsu ķermeņa temperatūra? "))

if temp<35.0: 
    print("Vai nav par aukstu?")

elif 35.0<=temp and 37.0>=temp:
    print("Viss kārtībā.")

else:
    print("Iespējams drudzis.")
"""

#------------------------------------------------
vieta = (input("Ievadi atrašanās vietu: "))

if vieta == "banka":
    print("te ir daudz naudas")

elif vieta == "veikals":
    print("jānopērk āboli")

elif vieta == "aptieka":
    print("man ir iesnas")

else:
    print("ābolu nav")
