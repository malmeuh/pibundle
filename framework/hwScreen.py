#!/usr/bin/python

## Most of the code below is from
# http://harizanov.com/2013/02/using-my-1-8-tft-as-a-raspberry-pi-status-display/

import pygame
import time
from time import strftime
import os

# TODO: Add a method to display a picture, for instance from opencv


class PiScreen:
    def __init__(self, size=(160, 128)):
        #Set the framebuffer device to be the TFT
        os.environ["SDL_FBDEV"] = "/dev/fb0"
        pygame.init()  # Already calls the font.init()

        self.size = size
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        pygame.mouse.set_visible(0)
        self.screen = pygame.display.set_mode(self.size)

        # Do some things on the screen to play around
        self.clear()

        print('Screen initialized')

    def clear(self):
        self.screen.fill(self.black)

    def fill(self, color):
        """
        :param color: 3 tuple
        """
        self.screen.fill(color)

    def display_time(self):
        self.clear()

        font = pygame.font.Font(None, 50)
        now = time.localtime()

        for setting in [("%H:%M:%S", 60), ("%d  %b", 10)]:
            timeformat, dim = setting
            current_time_line = strftime(timeformat, now)
            text = font.render(current_time_line, 0, (0, 255, 0))
            surf = pygame.transform.rotate(text, -90)

            self.screen.blit(surf, (dim, 20))

    def display_text(self, text, size=20, line=1, color=(255, 0, 0), clear_screen=False):
        """Used to display text to the screen. displayText is only configured to display
        :param text: string
        :param size: int (in pixels)
        :param line: int (in pixels)
        :param color: 3-tuple, between 0 and 255
        :param clear_screen: bool
        :type self: screen object
        """
        
        if clear_screen:
            self.clear()

        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        text_rotated = pygame.transform.rotate(text, -90)
        textpos = text_rotated.get_rect()
        textpos.centery = self.size[1]/2

        if line == 1:
            textpos.centerx = self.size[0]/2
            self.screen.blit(text_rotated, textpos)

        elif line == 2:
            textpos.centerx = 40
            self.screen.blit(text_rotated, textpos)

    def display_pict(self, pict):
        """
        :param pict: a numpy array, representing the picture to be displayed
        """

        self.clear() # Useful if the picture is smaller than the screen ?

        # TODO: Check the array type and its size, resize if needed
        # TODO: Draw directly using OpenCV ?

        surface = pygame.Surface(self.size)
        pygame.surfarray.blit_array(surface, pict)

        self.screen.blit(surface, self.size)