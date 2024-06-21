from pygame import *
import os
from Scripts.game import Game
import Scripts.constants
CUC = Game()
class App():
    def __init__(self):
        self.Cycle = True
        self.fps = 60
        self.window = display.set_mode(Scripts.constants.display_size,RESIZABLE)
        display.set_caption('Dooudle Jump')
        display.set_icon(image.load(os.path.join('assets','icons','icon.ico')))
        self.time = time.Clock()

    def run(self):
        while self.Cycle:
            self.handle_events()
            CUC.update_object()
            self.render()
            self.time.tick(60)


    def handle_events(self):
        for event2 in event.get():
            if event2.type == QUIT:
                self.Cycle = False
            if event2.type == KEYDOWN:
                CUC.process_key_down_event(event2.key)
            if event2.type == KEYUP:
                CUC.process_key_up_event(event2.key)
    def render(self):
        self.window.fill((0,0,0))
        CUC.render_object(self.window)
        display.update()