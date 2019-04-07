'''termcolor trial'''
#source code written by im.ri0t

import sys
import os
import random
import platform

from termcolor import colored, cprint

try:
    import colorama
    colorama.init()
except ImportError:
    pass

cprint('Hello! This is a trial of colored text in the terminal.', 'green', attrs=['blink'])
cprint('If you\'d like to try it out then press enter a few times.', 'blue', attrs=['bold'])
cprint('source code written by im.ri0t', 'red', attrs=['reverse'])
input()

def main():
    color_bank = [
        'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
    ]
    
    att_bank = [
        'bold', 'underline', 'dark', 'blink', 'reverse'
    ]

    color = random.choice(color_bank)
    att = random.choice(att_bank)
    
    cprint('Hello World!', color, attrs=[att])
    input()
    rep()

def rep():
    main()

if __name__ == '__main__':
    main()

#this should allow a random colored terminal output
