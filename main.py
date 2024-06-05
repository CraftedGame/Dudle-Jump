import pygame
from scripts.App import App

def Main():
    pygame.init()
    app = App()
    app.run()

if __name__ == '__main__':
    Main()