likedlist = ['everybody','people','courtesy','before','barricades','before']
for each_song in likedlist:
    print(each_song)
print()

tupleex = ('everybody','people','courtesy','before','barricades','before')
for each_song in tupleex:
    print(each_song)
print()

setex = {"everybody","people","courtesy","before","barricades","before"}
for each_song in setex:
    print(each_song)
print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for each_key in thisdict.keys():
  print(each_key)
print()

for each_value in thisdict.values():
  print(each_value)

def sayhello():
  print('Hello')
print(sayhello())