print("What phases do you see?")
a= input()
i=len(a)
print("\n Reversing...")
for i in range(len(a)-1,-1, -1):
  print(f"{a[i]}")
