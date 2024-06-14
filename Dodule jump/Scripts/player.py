import pygame
from Scripts.Sprites import Sprite
class Player(Sprite):
    def __init__(self,image,coords,jump_power,gravity,speed):
        super().__init__(image,coords)
        self.speed = speed
        self.jump_power = jump_power
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False
