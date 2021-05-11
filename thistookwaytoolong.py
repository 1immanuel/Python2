phonebook = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923',
  'James': '546-756-987',
  'Marge': '645-934-3425'

}
run = True

while run == True:

  print('1. Look up and entry.')
  print('2.Set and entry.')
  print('3. Delete an entry.')
  print('4. List all entries.')
  print('5. Quit.')

  action = int(input('What to do:'))

  if action == 1:
      search = input("What contaact are you looking for?")
      print(phonebook[search])
      

  elif action == 2:
      name = str(input('Enter contact name: '))
      number = str(input('Enter contact number: '))
      contact = (name, number)

      phonebook[contact] = {
        name, number
      }
      print(contact)

  elif action == 3:
      name = str(input("what contact do you want to delete? "))
      del phonebook[name]
      print("Contact %s deleted." % (name))

  elif action == 4:
      print(phonebook)

  elif action == 5:
      run = False
      print('Session Terminated')
  else:
      if action!= (1,5):
          print('Invalid Input')