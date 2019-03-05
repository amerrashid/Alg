import re

def test_num(cand: str):
    return re.match("^[0-9]+$", cand)

# def test_even(cand: str):
#     return re.match("^[]")

# def test_char (cand: str):
#     return re.match("^[A-Za-z]*$")

# def test_char (cand: str):
#     return re.match("^[A-Za-z]*$")