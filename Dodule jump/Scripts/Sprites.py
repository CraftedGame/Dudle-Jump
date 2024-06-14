from pygame import * 

class Sprite():
    def __init__(self,image,coords):
        self.image = image
        self.Rect = image.get_frect()
        self.Rect.center = coords

    def render(self,scene):
        scene.blit(self.image,self.Rect)

    def collide(self,other_rect):
        self.Rect.collide(other_rect)