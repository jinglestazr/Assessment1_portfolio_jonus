correct_pass='12345'
max_try=5
tries=0

while tries < max_try:
    pwd=input('Enter the Password: ')

    if pwd==correct_pass:
        print('ACCESS GRANTED. Welcome In !!!!')
        break 
    else:
        tries+=1
        left_tries=max_try-tries
        if left_tries>0:
            print(f'Incorrect Password. Please try again. You have {left_tries} attempts left.')
        else:
            print('Incorrect Password. Maximum try have been finished. The Owner has been contacted. Escape for your life.')
