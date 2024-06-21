from pygame import *
import os
from Scripts.Sprites import Sprite
from Scripts.functions import *
from Scripts.player import Player
class Game():
    def __init__(self):
        self.background = image.load(os.path.join('assets','images','background.png'))
        self.background = transform.scale(self.background, (1920,1080))
        self.platforms = [
            Sprite(load_images('assets','images','platform.png'),(200,700)),
            Sprite(load_images('assets','images','platform.png'),(100,450)),
            Sprite(load_images('assets','images','platform.png'),(380,250))
        ]
        self.player = Player(load_images('assets','images','player.png'),(240,600),15,0.4,4)

    def process_key_down_event(self,key):
        if key == K_a:
            self.player.is_walking_left = True
        if key == K_d:
            self.player.is_walking_right = True

    def process_key_up_event(self,key):
        if key == K_a:
            self.player.is_walking_left = False
        if key == K_d:
            self.player.is_walking_right = False

    def render_object(self,scene):
        scene.blit(self.background,(0,0))
        for i in self.platforms:
            i.render(scene)
        self.player.render(scene)

    def update_object(self):
        for i in self.platforms:
            if i.collide(self.player.Rect):
                self.player.on_platform = True
        self.player.update()