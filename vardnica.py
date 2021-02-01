#vārdnīcas jeb dictionaries
#atslēga:vērtība
tel = {
    "direktors": "27300486",
    "vietnieks": "25647731",
    "sekretāre": "27783009"
}
print(tel["sekretāre"])  #norādot atslēgu izdrukā vērtību
print(tel["direktors"])

cenas = {"piens": 1.12, "āboli": 0.95, "apelsīni": 1.89}

print(cenas["piens"])
print(cenas["apelsīni"])

d = {"k1": 123, "k2": [10, 11, 12], "k3": {"atsl1": 100, "atsl2": 200}}
#vārdnīcās var uzglabāt dažādus datu tipus
print(d["k3"]["atsl1"])  #izdrukā iekšējās vārdnīcas vērtību
print(d["k2"][2])  #izdrukā saraksta elementu

myDict = {"key1": ['a', 'b', 'c']}
print(myDict)
myList = myDict['key1']
print(myList)
burts= myList[2]
print(burts)
print(burts.upper())#izdrukā lielo C,kas atrodas vārdnīcas vērtībā
print(myDict["key1"][2].upper()) #vienā rindā atlasa elementu un pārveido

#pievieno jaunus objektus
newDict={"k1":100, "k2": 200}
print(newDict)
newDict["k3"]=300
print(newDict)
newDict["k1"]="simts"
print(newDict)