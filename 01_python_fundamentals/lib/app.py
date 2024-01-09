#!/usr/bin/env python3

# 📚 Review With Students:
# Python environment set up
# Python debugging tools
# Python datatypes

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

# 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# Note => Feel free to set your own values for "pet_mood" to view various outputs.

pet_mood = "Hungry!"
pet_name = "Rose"


# def hello_world():
#     monday = "need coffee"
#     print(monday)
#     ipdb.set_trace()  # pause the execution of code
#     # debugger here

#     not_interpreted_yet = "lunch"
#     print(not_intepreted_yet)


# hello_world()

# if pet_mood == "Hungry!":
#     print("Rose need to be fed.")
# elif pet_mood ="Rowdy":
#     print("Rose needs a walk")
# else:
#     print("test")

time = "morning"


if time == "morning":
    print("eat breakfast")
elif time == "afternoon":
    print("eat lunch")
elif time == "dinner":
    print("eat dinner")
else:
    print("go to sleep")


# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."

# Ternary Operator JS vs Python

# JS
# condition ? ture : false

# Python
# true, if condition else default val

print("eat breakfast") if time == "morning" else print("study python")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"


def say_hello(param="hello"):  # default argument
    print("hello, world")  # indentation is important


say_hello()

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"


def pet_greeting(name):
    return f"{name} says hello!"


print(pet_greeting("Rose"))


def schedule(time):
    if time == "morning":
        print(f"its {time} eat breakfast")
    elif time == "afternoon":
        print(f"its {time} eat lunch")
    elif time == "dinner":
        print(f"its {time} eat dinner")
    else:
        print("go to sleep")


print(schedule(time))

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."

# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.


def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        print(f"{pet_name} needs to be fed.")
    elif pet_mood == "Rowdy!":
        print(f"{pet_name} needs a walk.")
    elif pet_mood == "Relaxed":
        print(f"{pet_name} is all good.")
    else:
        print("???")


pet_status("Rose", "Relaxed")

counter = 0


def increment_counter():
    global counter
    counter += 10
    print(counter)


def double_counter():
    global counter
    counter *= 2
    print(counter)


increment_counter()
double_counter()

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"


def pet_birthday(number):
    try:
        number += 1
        return f"Happy Birthday! Your pet is now { number }."
    except TypeError:
        return "This is not a number"


print(pet_birthday(10))

# Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


print("------------------------------------")


name = "Steven"

print(f"Hi, {name}." if name != "Steven" else f"Goodbye, {name}.")
