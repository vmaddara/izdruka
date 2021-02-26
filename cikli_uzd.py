i = 1
while i <= 100:
    if i % 7 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 5 == 0:
        if i !=100:
            print("Fizz", end=", ")
        else:
            print("fizz", end="")
    elif i % 7 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
    i += 1
