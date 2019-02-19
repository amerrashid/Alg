import re

is_a_match = re.search("^jim$", "jim")
is_a_match2 = re.search("^jim$", "jom")

if re.search("^jim$", "jim"):
    print ("This is a match)"
else:
    print("Not a match")