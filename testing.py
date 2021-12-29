import re


def pwd(string):
    SpecialSym = ['$', '@', '#', '%']
    if len(string) < 6:
        print('length should be at least 6')
    if len(string) > 20:
        print('length should be not be greater than 20')
    if not any(char.isdigit() for char in string):
        print('Password should have at least one numeral')
    if not any(char.isupper() for char in string):
        print('Password should have at least one uppercase letter')
    if not any(char.islower() for char in string):
        print('Password should have at least one lowercase letter')
    if not any(char in SpecialSym for char in string):
        print('Password should have at least one of the symbols $ @ # %')
    else:
        print("Valid Password")


def name(string) :
    if any(char.isdigit() for char in string):
        print("Invalid Name")
    else:
        print("Valid Name")


def mob(string):      
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    if Pattern.match(string) :
        print("number is valid")
    else :
        print("number is invalid")
    

def email(string):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, string):
        print('Invalid Email Format')
    else:
        print("Valid Email Id")


def age(string):
    # if len(string) > 2 and any(a.isalpha() for a in string):

    # if not string.isdigit() and len(string) > 3 :
    #     print('Invalid Age')
    # else:
    #     print("Valid Age")

    if len(string) == 2:
        for i in string:
            if not i.isdigit():
                print('Not valid age')
        print("valid age")
    else:
        print("Not valid age")


def pin_code(string):
    if len(string) == 6:
        for i in string:
            if not i.isdigit():
                print('Not valid pincode')
        print("valid pincode")
    else:
        print("Not valid pincode")

# Correct
name("mohit")
pwd("Rohaan@2001")
mob("779874122a")   
email("324d")
age("23")
pin_code("400606")