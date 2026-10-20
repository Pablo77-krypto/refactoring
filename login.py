# second refactor

username = input('Enter username: ')
password = input('Enter password: ')

if username in users and users[username] == password:
    print('Logging successful')
else:
    print('Username not found or password incorrect')
