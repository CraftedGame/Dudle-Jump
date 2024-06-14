from pygame import *
import os
from Scripts.Sprites import Sprite
from Scripts.functions import *
class Game():
    def __init__(self):
        self.background = image.load(os.path.join('assets','images','background.png'))
        self.background = transform.scale(self.background, (1920,1080))
        self.platforms = [
            Sprite(load_images('assets','images','platform.png'),(200,700)),
            Sprite(load_images('assets','images','platform.png'),(100,450)),
            Sprite(load_images('assets','images','platform.png'),(380,250))
        ]
    
    def render_object(self,scene):
        scene.blit(self.background,(0,0))
        for i in self.platforms:
            i.render(scene)