def test(sequence):
  print("A: "+str(sequence))
  int(sequence)+3 #this doesn't change the outcome because the sequence in this line has not been defined and therefore won't be called when the program runs
  print("B: "+str(sequence))
  sequence = int(sequence)+3 #'sequence =' is what defined this line and allowed 10 to be added to 3 (Look at 'test(10)')
  print("C: "+str(sequence))

# fibinacci is a sequence of numbers
def fibinacci0():
  a = 0
  b = 1
  c = a+b #=1
  d = b+c #1+1=2
  e = c+d #1+2=3
  print(str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e))

# fibinacci is a sequence of numbers
def fibinacci1():
  #Step 1
  a = 0
  b = 1
  print(str(a))
  print(str(b))
  #Step 1.5
  c = a+b #=1
  print(str(c))
  #Step 2
  a = b #  <= KEY Term before it
  b = c # <= sum
  #Step 3 (At each new step the values of a and b take on the previous chunks summation)
  c = a+b #1+1=2
  print(str(c))
  a = b
  b = c
  c = a+b #1+2=3
  print(str(c))
  
def fibinacci2(end):
  #Step 1
  a = 0
  b = 1
  print(str(a))
  print(str(b))
  for each_step in range(0,end):
    c = a+b #0+1=1
    a = b 
    b = c
    print(str(c))

# 1 2 3 4 5 6 <- each_step 
# 0 1 1 2 3 5 8 13 .......... <- This value

# START MAIN PROGRAM: 
x = int(input("Give me a number. "))
test(10)
# fibinacci0()
# fibinacci1()
fibinacci2(x)