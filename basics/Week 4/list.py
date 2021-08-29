#Declare an empty list
red = []

#Declare a non-empty list
amber = ["Poland", "Portugal", "Romania", "Fiji", "Amber"]

#Printing full list
print(amber)

#Print a single element
print(amber[3])

#Add elements to the end of a list
red.append("Brazil")
red.append("Somalia")
red.append("Malta")

# for i in range(3):
#   red.append(input("Enter new re list country: "))

print(red)
#Insert data onto a list not at the end
red.insert(1, "Ghana")
print(red)
red.insert(3, "Switzerland")
print(red)

#Remove an item from the list by name
# red.remove(input("Which country to delete: "))
# print(red)

#Remove an item from list by index
red.pop(0)
print(red)
# bob = red.pop(1)
# amber.append(bob)
# print(red)
# print(amber)

#Delete an item
del red[1]
print(red)

#Slicing
print("---Slicing---")
print(amber[::2])
#Slicing allows you to specify start point (included), end point (excluded) and steps.

#Miroslav
a = "Python is lovely!"
print(a[::-1])
#Strings in Python ARE lists!!!!!(kind of)