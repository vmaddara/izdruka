''''vards = input("Kā tevi sauc? ")
print("Labdien, " + vards)

vecums = int(input("Cik tev ir gadu? "))     #0000
#print("Jums ir " + vecums + " gadi.")
print(f"Jums ir {vecums} gadi.")

print(f"Jūsu dzimšanas gads ir {2021 - vecums}.")
dzimGads = 2021 - vecums
print(f"Jūsu dzimšanas gads ir {dzimGads}.")

gradi = int(input("Cik pie jums ir grādi pēc celsija skalas? "))
print(f"Pie jums pēc fārenheita skalas ir {gradi * 9/5 + 32} grādi")

platums = float(input("Kāds jums ir istabas platums? "))
garums = float(input("Kāds jums ir istabas garums? "))
augstums = float(input("Kāds jums ir istabas augstums? "))
print=(f"Jūsu istabas tilpums ir {platums * garums * augstums}")

'''
#strings (rakstszīmju virknes)

print("sveiki")
print('sveiki')

print("I'm going for the run")
print('arī šis ir "risinājusm"')
print("Sveika, \npasaule!")  #drukā divās rindās
print("Sveika, \tpasaule!")  #drukā ar tabulācija atkāpi

#string garums - len() #0000
print(len("sveiki"))
print(len("čau ko tu dari?"))

#[sākums:beigas:solis]
myString="Sveika, pasaule!"
print(myString)
print(myString[0]) #izdrukā 1 simblou
print(myString[6]) #izdrukā 7 simblou
print(myString[-1]) #izdrukā pēdējo simbolu
print(myString[13]) #idrukā 14 rakstszīmi
print(myString[-3]) #idrukā 14 rakstszīmi

myString="abcdefghijklmnoprstuvz"
print(myString[2])
print(myString[2:]) #izdrukā visu sākot no 2 simbola(sākot no c)
print(myString[:3]) #izdrukā līdz 3. indeksam neieskaitot
print(myString[3:6]) #izdrukā no 3. līdz 6. neieskaitot (līdz 5.)  #000
print(myString[::]) #izdrukā visu
print(myString[::2]) #izdrukā katru 2. rakstzīmi
print(myString[2:7:2]) #izdrukā no 2. līdz 6. indekasm katru otro rakstzīmi
print(myString[::-1]) #izdrukā visu tikai no otras puses
print(myString[::-2]) #izdrukā katru 2. no otra gala