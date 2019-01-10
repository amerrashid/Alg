import datetime

def writelog (filename, string, severity = "I"):

    if severity != "I" and severity != "W" and severity != "E":
        raise Exception ("Error! We need to provide a valid severity of E W or I")

    current_date_time = datetime.datetime.now()

    with open (filename, "a+") as my_file:
        my_file.write(str(current_date_time) + " " + severity + " " + string + "\n")