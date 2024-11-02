# create a simple program that asks the user a question, evaluates their answer, and provides feedback.

'''ADVANCED REQUIREMENTS'''

name=input('Enter your name: ')
print('Hey',name,',Welcome to a small trivia of the capitals of 10 European Countries')

print() #added an empty print statement for having a space between a set of codes.
print('Question 1: ')
capital=input('Whats the Capital of France: ') #the program where the user can see the question and answer
if(capital.lower()=='paris'): #added .lower so that the python makes all user uppercase to lowercase.
    print('The answer you have given is correct') 
else:
    print('The answer you have given is incorrect')

print()
print('Question 2: ')
capital=input('Whats the Capital of Poland: ')
if(capital.lower()=='warsaw'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 3: ')
capital=input('Whats the Capital of Belgium: ')
if(capital.lower()=='brussels'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 4: ')
capital=input('Whats the Capital of Finland: ')
if(capital.lower()=='helsinki'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 5: ')
capital=input('Whats the Capital of Netherlands: ')
if(capital.lower()=='amsterdam'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 6: ')
capital=input('Whats the Capital of Hungary: ')
if(capital.lower()=='budapest'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 7: ')
capital=input('Whats the Capital of Estonia: ')
if(capital.lower()=='tallinn'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 8: ')
capital=input('Whats the Capital of Germany: ')
if(capital.lower()=='berlin'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 9: ')
capital=input('Whats the Capital of Portugal: ')
if(capital.lower()=='lisbon'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()
print('Question 10: ')
capital=input('Whats the Capital of Italy: ')
if(capital.lower()=='rome'):
    print('The answer you have given is correct')
else:
    print('The answer you have given is incorrect')

print()


