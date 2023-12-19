#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 10

    while count >= 1:
        print(count)
        count -= 1

    print("Happy New Year!")
happy_new_year()    
    



def square_integers(int_list):
    # code goes here!
    squared_list = [x ** 2 for x in int_list]
    return squared_list


list1 = [1, 2, 3, 4, 5]
list2 = [-1, -2, -3, -4, -5]

result1 = square_integers(list1)
result2 = square_integers(list2)

print("Squared elements of list1:", result1)
print("Squared elements of list2:", result2)

def fizzbuzz():
    # code goes here!
     for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()