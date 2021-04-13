def manipulateAString(myString):
  print("First Letter: "+myString[0])
  if(myString[0] == 'A'):
    myString = myString.replace('A', 'B')
    print(myString)

def manipulateArray(myArray):
  print("First Letter: "+str(myArray[0]))
  if(myArray[0] == 'A'):
    myArray[0] = 'B'
    print(str(myArray))

manipulateAString("ABC")
tisAnArray = ['A', 'B', 'C']
manipulateArray(tisAnArray)