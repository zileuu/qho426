x= int(input( "How many bars should be charged?  "))

i=0
y= "\u275A"
while (i<x):
  i=i+1
  print("Charging ",y* i )

--------------------------------------------------
  print("What phases do you see?")
a= input()
i=len(a)
stringopposit= []
index=len(a)
print("\n Reversing...")
for i in range(len(a)-1,-1, -1):
  stringopposit+=a
  print(f"{a[i]}")