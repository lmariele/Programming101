import random

def getFortune(number):
  print(number)
  if number == 1:
    return "OOF"
  if number == 2:
    return "Maybe... "
  if number == 3:
    return "Yep!"

# x = random.randint(1,3)
# print(x)
# fortune = getFortune(x)
# print(fortune)
print(getFortune(random.randint(1, 3)))