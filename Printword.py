import os
import time

from pyfiglet import Figlet

f = Figlet(font='Random')
word = 'Banamali Jena'
curr_word = ''
for char in word:
    os.system('reset') #assuming the platform is linux, clears the screen
    curr_word += char;
    print(f.renderText(curr_word))
    time.sleep(2)