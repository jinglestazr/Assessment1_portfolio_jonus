names=['Jake',"Zac", "Ian", "Ron", "Sam", "Dave"]

search= ('Sam')
if search in names:
    print('The person you are looking for is found in the list.') 
else:
    print('The person your looking for is unfortunatly not in the list.')

name=input('Enter the persons name you want to check: ')
if (name.lower()==name for name in names):
    print('The person your looking for is in the list.')
else:
    print('The person your looking for is not in the list unfortunatly')
