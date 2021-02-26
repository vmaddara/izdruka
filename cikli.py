#while True:
#    print("sveiki")  bezgalīgi ilgi pilda darbību

i = 1  #tipisks cilka mainīgais
while i <= 5:
    print("labi")
    i += 1  #i=1+1
print("i tagad ir", i)

j = 0
while j < 5:
    print("Nr", j)
    j += 1

while i > 0:
    print("skaitām apakaļ", i)
    i -= 1

#ar soli 2
i = 20
while True:
    if i > 26:
        break
    print("i ir", i)
    i += 2

h = int(input("norādi stāvus: "))
i=0
while i < h:
    print("*"*h)
    i += 1




i=0
while i<=100:
    if i%5==0:
       print("Fizz")
    elif i%7==0:
        print("Buzz")
    elif i%7==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)
    i+=1