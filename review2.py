meetings = int(input("How many meetings do I have today? "))
if meetings >=0 and meetings <=6:
  print("Don't forget that you have 5 meetings. ")
else:
  print("You have too many meetings. ")
for each_step in range(0,meetings):
  print(each_step)
x = meetings
while x !="0":
  print(x)
  x = input("Why so many meetings? ")
  print("blue"+"red") #this is an example of concatonating
  print("\"Leanna\'s mental health is struggling with meetings.\" ") #this is an example of escape characters, which allow the program to ignore the next characters
tired = ["cansada","suenos","tarde"]
for each_word in tired:
  print(each_word)