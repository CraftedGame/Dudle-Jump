from pygame import *
import os
from Scripts.game import Game
CUC = Game()
class App():
    def __init__(self):
        self.Cycle = True
        self.fps = 60
        self.window = display.set_mode((480,720),RESIZABLE)
        display.set_caption('Dooudle Jump')
        display.set_icon(image.load(os.path.join('assets','icons','icon.ico')))
        self.time = time.Clock()

    def run(self):
        while self.Cycle:
            self.handle_events()
            self.render()
            


    def handle_events(self):
        for event2 in event.get():
            if event2.type == QUIT:
                self.Cycle = False
            
    def render(self):
        self.window.fill((0,0,0))
        CUC.render_object(self.window)
        display.update()