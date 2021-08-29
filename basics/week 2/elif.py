age = int(input("What is your age: "))

if age < 20:
  print ("You are a child")
elif age > 65:
  print("You are old mate!")
elif age <= 30 and age >= 20:
  print("You are a grown up child")
else:
  print("You are an adult")