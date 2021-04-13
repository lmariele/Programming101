cosas = {
  "bee": "abeja",
  "pumpkin": "calabaza",
  "owl": "búho",
} 

def translate0(word):
  print(cosas[word])

def translate():
  word = input("Word2. ")
  print(cosas[word])

def printEntireDictionary():
  print(cosas)

def addWord():
  x = input("Let\'s add a word. ")
  y = input("Now, let\'s add a definition. ")
  cosas[x] = y

# palabra = str.lower(input("Word1. "))
# print("Translate Without Input variable")
# translate()
# translate()
# translate()

# print("Translate Original with input variable")
# translate0(palabra)
# translate0(palabra)
# translate0("pumpkin")



fileWriter = open("spanishdictionary.txt","w") #w allows the user to write to the file
fileWriter.write(str(cosas))
fileWriter.close()

fileReader = open("spanishdictionary.txt")
contents = fileReader.read()
fileReader.close()
print(contents)

cosas["new"] = "nueva"
addWord()
fileWriter1 = open("spanishdictionary.txt","w")
fileWriter1.write(str(cosas))
fileWriter1.close()

fileReader = open("spanishdictionary.txt")
contents = fileReader.read()
fileReader.close()
print(contents)

#next step is to create functions so streamline 35-53