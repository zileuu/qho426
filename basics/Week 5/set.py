#Initialise empty set
set1 = set()
#Initialise non-empty set
colors = {"blue", "red","black","yellow"}
#Add elements to a set
set1.add("purple")
set1.add("green")
set1.add("pink")
set1.add("yellow")
#Check membership
if "pink" not in set1:
  print("Set1 does not contain PINK color")
#Union of sets (joining)
print(set1 | colors)
print(set1.union(colors))
#Intersection
print(set1&colors)
print(set1.intersection(colors))
#Set Difference - items in one set but not the other
print(set1 - colors)
print(set1.difference(colors))
print(colors - set1)
print(colors.difference(set1))

#Comprehension
numbers = {n for n in range(101) if n%2 == 0}
l_numbers = [n for n in range(101) if n%2 == 1]
print(numbers)
print(l_numbers)
#Conversion
lista = ["Piotr", "Tadek", "Aga", "Piotr", "Henry", "Piotr"]

print(len(lista))
set2 = set(lista) 
print(len(set2))