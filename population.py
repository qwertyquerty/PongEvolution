import math
import pygame as pg
v = pg.math.Vector2
from random import randint, choice
from config import *

from sprites import Ball, Paddle
from neuralnet import Neural_Network

class Population():
    def __init__(self, size, game):
        self.players = []
        self.size = size
        self.highscore = 0
        self.generation = 1
        self.winner = None
        for i in range(size):
            self.players.append(Player(game,self))

        self.living = len(self.players)

    def update(self):
        for player in self.players:
            if player.alive:
                player.update()

    def gen(self):
        players = sorted(self.players, key=lambda x: x.score)[::-1]
        players = players[:len(players)//2]
        children = []
        for player in players:
            player.reset()
            child = player.copy()
            child.neural_net.mutate(MUTATION_RATE)
            children.append(child)

        self.players = players+children
        self.generation += 1
        self.living = len(self.players)


class Player():
    def __init__(self, game, pop):
        self.pop = pop
        self.game = game
        self.ball = Ball(game)
        self.ball.player = self
        self.paddle = Paddle(game,self.ball)
        self.paddle.player = self
        self.alive = True
        self.neural_net = Neural_Network(5,2,HIDDENNODES,1)
        self.score = 0
        self.color=(int(randint(0,POPULATION_SIZE)*(200/POPULATION_SIZE)+50),int(randint(0,POPULATION_SIZE)*(200/POPULATION_SIZE)+50),int(randint(0,POPULATION_SIZE)*(200/POPULATION_SIZE)+50))

    def reset(self):
        self.score = 0
        self.alive = True
        self.ball.reset()
        self.paddle.reset()

    def copy(self):
        c = Player(self.game,self.pop)
        c.neural_net = self.neural_net.copy()
        c.color = self.color
        return c

    def die(self):
        self.score = self.game.score
        self.alive = False
        self.pop.living -= 1
        if self.score > self.pop.highscore:
            self.pop.highscore = self.score
        if self.pop.living == 0:
            self.pop.winner = self

    def update(self):
        input = [
            -1 if self.paddle.pos.x > self.ball.pos.x else 1,
            (self.ball.pos.y - HALFSCREENSIZE[1])/HALFSCREENSIZE[1],
            self.ball.vel.x,
            self.ball.vel.y,
            (self.paddle.pos.x - HALFSCREENSIZE[0])/HALFSCREENSIZE[0]
        ]
        choices = self.get_choices(input)
        self.paddle.pos.x += abs(choices[0]*PLAYERSPEED)
        self.paddle.pos.x -= abs(choices[1]*PLAYERSPEED)
        self.ball.update()
        self.paddle.update()

    def get_choices(self,input):
        return self.neural_net.run(input)
