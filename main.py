import pygame as pg
from util import show_player_net
from game import Game

from config import *

screen = pg.display.set_mode(SCREENSIZE, pg.DOUBLEBUF|pg.HWACCEL|pg.HWSURFACE)
screen.set_alpha(None)
pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])


g = Game()
clock = pg.time.Clock()

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LSHIFT:
                for player in g.population.players:
                    if player.alive:
                        player.die()
            if event.key == pg.K_LALT:
                if g.population.winner:
                    show_player_net(g.population.winner)



    keys = pg.key.get_pressed()
    g.update()
    g.draw(screen,keys[pg.K_w])
    clock.tick(FPS_CAP)
