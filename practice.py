phonebook = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923',
  'James': '546-756-987',
  'Marge': '645-934-3425'

}

def one():
  search = input("What contact are you looking for?")
  return phonebook[search]

def two():
  name = str(input('Enter contact name: '))
  number = str(input('Enter contact number: '))
  phonebook[name] = number
  return phonebook[name]

def three():
  name = input("what contact do you want to delete? ")
  del phonebook[name]
  return "Contact %s deleted." % (name)

def four():
  print(phonebook)

run = True

while run == True:

  print('1. Look up and entry.')
  print('2.Set and entry.')
  print('3. Delete an entry.')
  print('4. List all entries.')
  print('5. Quit.')

  action = int(input('What to do:'))

  if action == 1:
    print(one())

  elif action == 2:
    print(two())

  elif action == 3:
    print(three())

  elif action == 4:
    print(four())

  else:
    if action == 5:
      run = False
      print('Session Terminated')