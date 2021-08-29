
print("What is your name?")
name = input()
#when you use input() functon, the default data type is a string!
print("How old are you?")
age = int(input())

print("How tall are you (in meters)")
height = float(input())

print("How much to you weight (in kg)")
weight = float(input())

bmi = weight / (height **2)

#print(f"{name} you are {age} years old and your bmi is {bmi}")
#concatenation of strings (join them together)
#print(name +" you are " + str(age) + " years old and your bmi is " + str(bmi) )
print("{} you are {} years old and your bmi is {:.2f}".format(name, age, bmi))