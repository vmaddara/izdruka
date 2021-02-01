#lists jeb saraksti
#["Sveika",100,"tu", 3.59, "skaista!", [1,26]]
myList = [1, 2, 3, 100, "tu", 3.59, "skaista!"]
print(len(myList))  #saraksta garums

my_list = ["viens", "divi", "trīs", "četri"]
print(my_list[0])  #izdrukā elementu ar norādīto indeksu
print(my_list[2])
print(my_list[1:])  #izdrkā no norādītā indeksa līdz beigām

#sarakstu apvienošana jeb konkatinācija
cits_list = ["pieci", "seši"]
print(my_list + cits_list)  #izdrukā ar sarakstu ar abu mainīgo elementiem
jauns_list = my_list + cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0] = 1  #aizstāj konkrēto elementu
print(jauns_list)

jauns_list.append("septiņi")  #pievieno pēdējo elementu
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

pop_elem = jauns_list.pop()  #noņem elementu ar norādīto indeksu
print(jauns_list)
print(pop_elem)

#elementu kārtošana
new_list = ['b', 'a', 'z', 'e']
num_list = [4, 1, 8, 3]
print(new_list)  #sakāto oēc alfabēta
new_list.sort()
print(new_list)
print(num_list)
num_list.sort(
)  #sakārto, Bet jāizzmanto kā atsevišķa metode, to nevar izmanto skā darbību
print(num_list)
num_list.reverse()  #sakārto pretējā secībā
print(num_list)
myList = [
    1,
    2,
    3,
    100,
    3.59,
]
myList.sort()
print(myList)

#saraksts sarakstā(nested)
nestedList = [1, 5, [7, 2]]
print(nestedList[2][1])

#uzdevumi
augli = ["ābols", "banāns", "gurķis"]
print(augli[2])

augli[2] = "apelsīns"
print(augli)

augli.append("bumbieris")
print(augli)

augli.insert(2, "citrons")  #insert
print(augli)

augli.pop(1)
print(augli)

print(f"Sarakstā ir {len(augli)} dažādi augļi.")
augli.sort()
print(augli)


