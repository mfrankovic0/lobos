#    _       _               
#   | | ___ | |__   ___  ___ 
#   | |/ _ \| '_ \ / _ \/ __|
#   | | (_) | |_) | (_) \__ \
#   |_|\___/|_.__/ \___/|___/
#                            
# A serial number generator for [/REDACTED]/


import random
import string

header = "MXL"
ff = ''
lt = ''

def firstfour():
    global ff
    digits = string.digits
    ff = ''.join(random.choice(digits) for i in range(4))
    
def lastthree():
    global lt
    letters = string.digits + string.ascii_uppercase
    lt = ''.join(random.choice(letters) for i in range(3))
    
    
firstfour()
lastthree()

serial = header + ff + lt

print(serial)
