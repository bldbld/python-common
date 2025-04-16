'''
Created on 2010-4-20

@author: bkin
'''
import sys
import pygame
import threading
import random

class Game:
  def _init_(self):
    pygame.init()
    
  def Start(self):
    self.screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame')
    self.image = pygame.image.load('image/cover.jpg')
    rect = self.image.get_rect()
    rect.left = 200 * (+1) + rect.left
    rect.top = 400
    self.screen.blit(self.image, (200, 100, 400, 140))
    start = 1
    while start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        else:
          pass
        
if __name__ == "__main__":
  game = Game()
  game.Start()
