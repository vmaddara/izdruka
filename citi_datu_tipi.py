#tuples-līdzīgs list, bet nav mainīgs, izmanto parastās (iekavas), sakārtots
my_tup = (1, 2, 3)
my_list = [1, 2, 3]
print(type(my_tup))
print(type(my_list))
print(len(my_tup))

#var saturēt dažādus datu tipus
my_tup = ("es", 6, 6, 2.58, 6)
print(my_tup)

#var indeksēt
print(my_tup[0])
print(my_tup[-1])

#metodes
print(my_tup.count(6))  #saskaita cik reizes atkārtojas konkrētais objekts
print(my_tup.index(6))  #parāda indeksu, kur pirmoreiz parādās objekts

#nav maināms
my_list[0] = "viens"
print(my_list)
#my_tup[0]="1"       #nav iespējams

#---------------------------------------#
#sets- nesakārtota unikālu objektu kopa
my_set = set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(1.26)
print(my_set)
my_set.add(2)  #katrs elements ir tikai vienu reizi
print(my_set)
my_list = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3,
    3
]
print(set(my_list))

#piemērs
s = "Salaspils"
my_set = set(s)
print(my_set)

#-----------------------------------------#
#booleans- True vai False-izmanto loģiskajos operātoros
print(True)  #ar lielo burtu
print(type(False))

#piemērs
print(1 > 2)
print(1 == 1)
