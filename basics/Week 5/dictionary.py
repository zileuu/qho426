git#Initialise empty dictionary
phonebook = {}
#Initialise non-empty dictionary
piotr_data = {"Name": "Piotr", "Age":88, "Doggo": False}
#Search a dictionary
print(piotr_data["Doggo"])
#Populate the dictionary
phonebook["Frank"] = 7364837463647
phonebook["Loki"] = 888888888
phonebook["Haga"] = 274825436825478
phonebook["Loki"] = 273237263726
print(phonebook)
#Populating dictionary more efficiently
# for i in range(5):
#   phonebook[input("Enter the name: ")] = input("Enter the number: ")
# print(phonebook)
#Accessing by value
for i in piotr_data.items():
  print(i)

  lista=[]
for i in piotr_data.values():
  lista.append(i)