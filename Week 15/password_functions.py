import re


complex_enough = validate_password_length(password)

def validate_password_length(password: str):

    if not re.match("^.{8,}", password):

        complex_enough = False

    return True

def validate_password_lowercase (password:str):
    if not re.match("[a-z]", password):

        complex_enough = False
    return True

def validate_password_uppercase (password:str):
    if not re.match("[A-Z]", password):

        complex_enough = False
    return True

def validate_password_symbol (password:str):
    if not re.match("[^0-9A-Za-z\s]", password):
        complex_enough = False
    return True

def validate_password_nospaces(password:str):
    if re.match("\s", password):
        complex_enough = False

return complex_enough



