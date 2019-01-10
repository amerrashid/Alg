import time
from logger import writelog

try:
    writelog ("logfile1.log", "Program started.", "O")

    time.sleep (5)

    writelog ("logfile1.log", "Program finished.")
except Exception as error:
    print ("Oh no! And error has occured")
    print(error)