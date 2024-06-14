import pygame
import os
def load_images(*paths):
    path = os.path.join(*paths)
    image = pygame.image.load(path)
    image.set_colorkey((0,0,0))
    return image