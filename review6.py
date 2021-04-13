import random
x = random.randint(1, 3)
y = random.randint(1, 3)
z = int(input("Give us a number. "))
if x < y:
  print(str(y)+" is greater than "+str(x))
  if z > 0:
    print("z is "+str(z))
if x > y:
  print(str(x)+" is greater than "+str(y))
if x == y:
  print("they are equal "+str(x))