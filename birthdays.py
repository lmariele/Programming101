birthdays = {'Leanna':'Dec 23', 'Megan':'Sep 21', 'Michael':'Apr 8'}

while True:
  print('Enter a name :')
  name = input('(Blank to quit)')
  if name =='':
    break

  if name in birthdays:
    print(birthdays[name]+' is the birthday of '+name)
  else:
    print('I don\'t remember '+name+'\'s birthday. ')
    bday = input('What is their birthday? ')
    birthdays[name] = bday
    print('Birthday database updated. ')
    #tab to shift highlighted section to the right and tab+shift to shift highlighted section to the left