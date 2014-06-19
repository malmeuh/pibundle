#!/usr/bin/python

## Most of the code below is from
# http://harizanov.com/2013/02/using-my-1-8-tft-as-a-raspberry-pi-status-display/

import pygame
import time
from time import strftime
import os


# Add a method to display a picture, for instance from opencv

class PiScreen:
    def __init__(self):
        #Set the framebuffer device to be the TFT
        os.environ["SDL_FBDEV"] = "/dev/fb1"

        pygame.init()

        self.size = [128, 160]
        self.black = 0, 0, 0

        pygame.mouse.set_visible(0)
        self.screen = pygame.display.set_mode( self.size )

        # Do some things on the screen to play around
        self.clear()

        return 'Screen initialized'

    def clear(self):
        self.screen.fill((0, 0, 0))

    def fill(self, r, g, b):
        self.screen.fill(r, g, b)

    def display_time(self):
        self.clear()

        font = pygame.font.Font(None, 50)
        now = time.localtime()

        for setting in [("%H:%M:%S", 60), ("%d  %b", 10)]:
            timeformat, dim = setting
            current_time_line = strftime(timeformat, now)
            text = font.render(current_time_line, 0, (0,250,150))
            surf = pygame.transform.rotate(text, -90)

            self.screen.blit(surf, (dim, 20))

    def display_text(self, text, size, line, color, clear_screen):
        """Used to display text to the screen. displayText is only configured to display
        two lines on the TFT. Only clear screen when writing the first line"""
        if clear_screen:
            self.clear()

        font = pygame.font.Font(None, size)
        text = font.render(text, 0, color)
        text_rotated = pygame.transform.rotate(text, -90)
        textpos = text_rotated.get_rect()
        textpos.centery = 80

        if line == 1:
            textpos.centerx = 90
            self.screen.blit(text_rotated, textpos)

        elif line == 2:
            textpos.centerx = 40
            self.screen.blit(text_rotated, textpos)
