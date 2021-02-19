#if, else, elif
'''
if nosacījums:
    izpildāmās darbības
elif cits nosacījums:
    izpildāmās darbības
else :
    izpildāmās darbības visos citos gadījumos
'''
a=0
if a>5:
    print(f"skaitlis {a} ir lielāks par 5")
elif a>0:
    print(f"skaitlis {a} ir lielāks par 0")

else:
    print(f"skaitlis {a} ir negatīvs")

if True:
    print("patiesi")

suns_grib_est= False

if suns_grib_est:
    print("Pabaro suni!")
else:
    print("Suns ir paēdis.")
