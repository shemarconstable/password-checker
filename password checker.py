'''
TODO: Match password with parameters of 8 char, 1 digit,upper and lower

'''
#this password checker uses the standard 8 letter, upper lower case with at least 1 digit
while True:
    import re
    password = input('Enter a password to test: ')

    length = re.compile(r'.{8,}')
    ucase = re.compile(r'[A-Z]')
    lcase = re.compile(r'[a-z]')
    digit= re.compile(r'[0-9]')

    if(length.search(password) is not None and ucase.search(password) is not None and lcase.search(password) is not None and digit.search(password) is not None):
        print('your password is good mate')
    else:
        print('get a better password scrub')
    stop=input('continue?[y/n]: ')
    if stop=='n':
        break
