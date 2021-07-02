
str1= (input("Where Should I look: "));
if (str1== "in the bedroom"):
   b= (input("where in the bedroom should I look: "))
   if (b== "under the bed"):
     print ("Found some shoes but no battery")
   if (b!= "under the bed"):
      print("Found some mess but no batery")
if (str1 == "in the bathroom"):
   a= (input("Where in the bathroom should I look: "))
   if (a == "in the bathhub"):
    print("rubber ducker but no batery")
   if(a!= "in the bathhub"):
      print("Found wet surface but no battery")
if (str1 =="in the lab"):
  c= (input("Where in the lab should I look: "))    
  if(c == "on the table"):
    print("yes I found the battery")
  if( c!= "on the table"):
    print("Found some tools but no battery")
else:
  print("I dont know where is that but i will keep looking")

  