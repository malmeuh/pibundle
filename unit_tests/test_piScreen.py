__author__ = 'benjamin lefaudeux'

import sys
sys.path.insert(0, '../framework')

import hwScreen as hw

screen = hw.PiScreen()
screen.clear()
screen.display_text('Hello world !')
# screen.display_time()
print "Time displayed ?"
raw_input('Press any key to quit')

