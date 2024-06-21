import pygame
from Scripts.Sprites import Sprite
class Player(Sprite):
    def __init__(self,image,coords,jump_power,gravity,speed):
        super().__init__(image,coords)
        self.original_image = image.copy()
        self.speed = speed
        self.jump_power = jump_power
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False
        self.velocity_y = 0
        self.on_platform = False

    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.Rect.y += self.velocity_y

        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.Rect.x -= self.speed
                self.image = pygame.transform.flip(self.original_image,True,False)
            else:
                self.Rect.x += self.speed
                self.image = self.original_image.copy()

        if self.on_platform:
            self.velocity_y =- self.jump_power
            self.on_platform = False