import math
import pygame as pg
v = pg.math.Vector2
from random import randint, choice
from config import *

from population import Population





class Game():
    def __init__(self):
        self.population = Population(POPULATION_SIZE,self)
        self.score = 0
        self.ballspeed = DEFAULT_BALLSPEED

    def update(self):
        self.ballspeed += DIFFICULTY_RATE
        self.population.update()
        self.score += 1

        if self.population.living == 0:
            self.score = 0
            self.ballspeed = DEFAULT_BALLSPEED
            self.population.gen()

    def draw(self,surf,winner_only=False):
        surf.fill(BLACK)
        if not winner_only:
            for player in self.population.players:
                if player.alive:
                    pg.draw.rect(surf,player.color,player.paddle.rect,2)
                    pg.draw.circle(surf,player.color,(int(player.ball.pos.x),int(player.ball.pos.y)), BALLRADIUS, 2)
        else:
            winner = self.population.winner
            if winner and winner.alive:
                pg.draw.rect(surf,winner.color,winner.paddle.rect,2)
                pg.draw.circle(surf,winner.color,(int(winner.ball.pos.x),int(winner.ball.pos.y)), BALLRADIUS, 2)

        surf.blit(font.render("Generation: {}".format(self.population.generation), False, WHITE), (0,0))
        surf.blit(font.render("Score: {}".format(self.score), False, WHITE), (0,20))
        surf.blit(font.render("Alive: {}/{}".format(self.population.living,self.population.size), False, WHITE), (0,40))
        surf.blit(font.render("Highscore: {}".format(self.population.highscore), False, WHITE), (0,60))
        pg.display.flip()
