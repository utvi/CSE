'''
print ("Hello World")

# This is a comment. I can write whatever I want
# Here and it won't do anything about it.
#It has no effect on the code.
print()  # This addsextra spaces on the terminal
print("This will print here. Notice the spacing")

a = 4
b = 3
print(a + b)
print(a*5)
print(5-3)
print(6/5)  # Results in a float (with decimals)

print("Figure this out")
print(6 // 4)  # Results in an integer (without decimal)
print(12 // 3)
print(9 // 4)

print(6 % 4)
print(5 % 3)
print(9 % 4)

car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 1024
car_mpg = 0.01

print("I have a car called %s. It's pretty nice" % car_name)

# Input
# name = input("What is your name? ")
# print("Hello %s" % name)

# Auto-comment - ctrl + /
# age = input ("How old are you?")
# print("%s?! You belong in a museum. " % age)

# Hidden age
real_age = int(input("How old are you? >_"))
hidden_age = real_age + 5
print(hidden_age)
print("%d is incredibly old. You are actually %d old" % (hidden_age, real_age))
'''

# functions
def printHelloWorld():
     print("Hello World!")


printHelloWorld()
'''
 This is a multi-line comment
 I can type anywhere here.
 '''

# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)

# loops
for i in (1,2,3):
    printHelloWorld()

print()
for i in range (3):
    printHelloWorld()

print()
for i in range(5):  # Range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)


# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same thing as a = a + 1

'''
Hints with loopa
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
'''

# # Random numbers
# import random  # This should always be on line 1
# print(random.randint(0, 100))
#
# # Control Statements
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 70:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc())
#
# # Equality Statements
# print(5 > 3)
# print(5 >= 3)
# print(3 == 3)
# print(3 != 4)

'''
a = 3 # A is set to 3
a == 3 # Is equal to 3?
'''

# Lists
shopping_list = ["milk", "PC", "Eggs", "Xbox One", "PS4"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a list
shopping_list[0] = "milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for item in shopping_list:
    print(item)

'''
1. Make a list
2. change the third thing in the list
3. print the item
4.print the list
'''

new_list = ["egg", "cheese", "oranges", "raspberries"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list) -1])
print(new_list)

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])

# Adding things to the list
christmas_list = []  # ALWASY USE SQUARE BRACKETS
christmas_list.append("Tacos")
christmas_list.append("Bumblebee")
christmas_list.append("Red Dead Redemption 2")
print(christmas_list)

# Noice this is an "object.method(Parameters)"

# Removing things from a list
christmas_list.remove("Tacos")
print(christmas_list)

'''
1. make a new list with 3 items
2. add a 4th item to the list
3. remove one of the first three itms from the list
'''
practice_list = ["chair", "bacon", "bear"]
practice_list.append("hairspray")
practice_list.remove("bacon")
print(practice_list)

# also removing things from a list
christmas_list.pop(0)  # removes the item at index 0
print(christmas_list)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet',
          'purple', 'black', 'grey', 'brown', 'gold', 'pink', 'cyan',
          'white', 'turquoise']
print(len(colors))

# find the index
print(colors.index("gold"))

# changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "u":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")

# changing lists into strings
print("".join(list1))
