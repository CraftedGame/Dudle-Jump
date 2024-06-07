from pygame import *
import os
class Game():
    def __init__(self):
        self.background = image.load(os.path.join('assets','imges','background.png'))