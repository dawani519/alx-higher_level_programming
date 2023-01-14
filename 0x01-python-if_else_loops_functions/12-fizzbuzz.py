#!/usr/bin/python3
def fizzbuzz():
    for number in range(0, 101):
        if number == number % 3:
            print("{Fizz}".format(number))
            if number == number % 5:
                print("{Buzz}".format(number))
            elif number == number % 3 and number = number % 5:
                print("{FizzBuzz}".format(number))
            else:
                print("{}".format(number), end=" ")

