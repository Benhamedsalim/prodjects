import re
def isEmail(email):
    is_email = re.search(r"^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$", email)
    if is_email:
        print(f'Email {email} is valid')
    else:
        print(f'Email {email} is not valid')



print('Is hsoub.academy@gmail.com a email?')
isEmail('hsoub.academy@gmail.com')
print('Is hsoub.academy@gmail a email?')
isEmail('hsoub.academy@gmail')