'''  Create functions that can find out if number is prime, can find a prime number within a range of values and computes N, used in RSA encryption'''

def isPrime(number):
  for thing in range(2,number):
    if number % thing == 0:
      return False
  return True

def findPrime(start, end):
  for stuff in range(start, end+1):
    if isPrime(stuff):
      return stuff

def encrypt():
  x= int(input("Provide an integer: "))
  y= int(input("Provide a second integer (larger): "))
  p1 = findPrime(x,y)
  x= int(input("Provide an integer: "))
  y= int(input("Provide a second integer (larger): "))
  p2 = findPrime(x,y)
  return p1*p2