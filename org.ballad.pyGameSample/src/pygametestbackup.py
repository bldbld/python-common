import sys
import pygame
import threading
import random

class Game:
  def _init_(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Py game')
    self.image = []
    self.imagerect = []
    self.vs = pygame.image.load('image/vs.jpg')
    self.o = pygame.image.load('image/o.jpg')
    self.p = pygame.image.load('image/p.jpg')
    self.u = pygame.image.load('image/u.jpg')
    self.title = pygame.image.load('image/title.jpg')
    self.start = pygame.image.load('image/start.jpg')
    self.exit = pygame.image.load('image/exit.jpg')
    for i in range(3):
      jpg = pygame.image.load('image/'+str(i)+'.jpg')
      self.image.append(jpg)
    for i in range(3):
      image = self.image[i]
      rect = image.get_rect()
      rect.left = 200*(i+1)+rect.left
      rect.top = 400
      self.imagerect.append(rect)
  def Start(self):
    self.screen.blit(self.title, (200,100,400,140))
    self.screen.blit(self.start, (350,300,100,50))
    self.screen.blit(self.title, (350,400,100,50))
    pygame.display.filp()
    start = 1
    while start:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if self.isStart() == 0:
            start = 0
          elif self.isStart() == 1:
            sys.exit()
          else:
            pass
        else:
          pass
    self.run()
  def run(self):
    self.screen.fill((0,0,0))
    for i in range(3):
      self.screen.blit(self.image[i],self.imagerect[i])
    pygame.display.flip()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          self.OnMouseButDown()
        else:
          pass
  def isStart(self):
    pos = pygame.mouse.get_pos()
    if pos[0] > 350 and pos[0] < 450:
      if pos[1] > 300 and pos[1] < 350:
        return 0
      elif pos[1] > 400 and pos[1] < 450:
        return 1
      else:
        return 2
  def OnMouseButDown(self):
    self.screen.blit(self.vs, (300,150,140,140))
    pos= pygame.mouse.get_pos()
    if pos[1] > 400 and pos[1] < 540:
      
      
        
if __name__ == "__main__":
  game = Game()
  game.Start()
