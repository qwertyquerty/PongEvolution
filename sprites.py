import math
import pygame as pg
v = pg.math.Vector2
from random import randint, choice
from config import *

class Ball():
    def __init__(self,game):
        self.game = game
        self.pos = v(randint(BALLRADIUS+10,SCREENSIZE[0]-BALLRADIUS-10),20)
        self.rect = pg.Rect(0,0,BALLRADIUS*2,BALLRADIUS*2)
        self.rect.center = (self.pos.x,self.pos.y)
        self.vel = v(choice([-1,1]),1)

    def update(self):
        self.pos.y += self.vel.y*self.game.ballspeed
        self.pos.x += self.vel.x*self.game.ballspeed

        if abs(self.vel.y*self.game.ballspeed)!=abs(self.vel.x*self.game.ballspeed):
            print(self.vel)
        self.rect.center = (self.pos.x,self.pos.y)

        if self.rect.right > SCREENSIZE[0]:
            self.vel.x = -1
            self.rect.right = SCREENSIZE[0]
        elif self.rect.left < 0:
            self.vel.x = 1
            self.rect.left = 0
        if self.rect.top < 0:
            self.vel.y = 1
            self.rect.top = 0
        elif self.rect.bottom > SCREENSIZE[1]:
            self.player.die()

        self.pos = v(*self.rect.center)


    def reset(self):
        self.pos = v(randint(BALLRADIUS+10,SCREENSIZE[1]-BALLRADIUS-10),20)
        self.rect = pg.Rect(0,0,BALLRADIUS*2,BALLRADIUS*2)
        self.rect.center = (self.pos.x,self.pos.y)
        self.vel = v(choice([-1,1]),1)

class Paddle():
    def __init__(self,game,ball):
        self.game = game
        self.ball = ball
        self.pos = v(SCREENSIZE[0]//2,SCREENSIZE[1]-20)
        self.rect = pg.Rect(0,0,PADDLESIZE[0],PADDLESIZE[1])
        self.rect.center = (self.pos.x,self.pos.y)

    def update(self):
        self.rect.center = (self.pos.x,self.pos.y)
        if self.rect.right > SCREENSIZE[0]: self.rect.right = SCREENSIZE[0]
        elif self.rect.left < 0: self.rect.left = 0

        if self.rect.colliderect(self.ball.rect):
            if (self.ball.rect.bottom - self.ball.vel.y*self.game.ballspeed) <= self.rect.top:
                self.ball.vel.y = -1
                self.ball.rect.bottom = self.rect.top
                self.ball.pos = v(*self.ball.rect.center)
            else:
                if self.ball.vel.x == 1:
                    self.ball.vel.x = -1
                    self.ball.rect.right = self.rect.left
                elif self.ball.vel.x == -1:
                    self.ball.vel.x = 1
                    self.ball.rect.left = self.rect.right
            self.ball.pos = v(*self.ball.rect.center)

        self.pos = v(*self.rect.center)

    def reset(self):
        self.pos = v(SCREENSIZE[0]//2,SCREENSIZE[1]-20)
        self.rect = pg.Rect(0,0,PADDLESIZE[0],PADDLESIZE[1])
        self.rect.center = (self.pos.x,self.pos.y)
