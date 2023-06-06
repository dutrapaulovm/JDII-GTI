# -*- coding: utf-8 -*-
from itertools import count
from tkinter import E
import pygame, sys
import numpy as np
import pandas as pd
import time
from MapaLevelObjects import *
from BaseGame import BaseProblem

from pygame import draw
from pygame import font
from pygame.locals import *
import csv

from utils import *

class MapaGame(BaseProblem):    

    def __init__(self, rows = 0, cols = 0, border = False, tile_size = 16):

        self.border = border
        self.tile_size = tile_size
        
        offset_border = 0
        
        if (self.border):
            offset_border = 2

        cols = cols + offset_border
        rows = rows + offset_border

        if cols > 0 and rows > 0:            
            self.width  = cols * self.tile_size
            self.height = rows * self.tile_size
        else:            
            self.width = 16 * self.tile_size
            self.height = 8 * self.tile_size        
        
        super(MapaGame, self).__init__(w = self.width, h = self.height, tile_w = self.tile_size, tile_h = self.tile_size, scale = 6)            

        #self.ffintelligent  = pygame.font.match_font("FFFIntelligent.ttf", 0, 0) #pygame.font.Font('freesansbold.ttf', 12)             

        self.fntHUD      = pygame.font.Font('freesansbold.ttf', 12)     
        self.fntSmallHUD = pygame.font.Font('freesansbold.ttf', 12)
        self.tiles             = {}
        self.tile              = 0
        self.reward            = 0
        self.tilesConnections  = ""
        self.right             = 0
        self.left              = 0
        self.up                = 0
        self.down              = 0
        self.state             = 0
        self.origem            = (0,0) 
        self.destino           = (0,0)
        self.h                 = 1
        self.player            = None
        self.action            = 0
        self.mapAux            = 0
        self.reached           = False
        self.tick_agent        = 0.1
        self.show_matriz       = True 
        
        for row in range(self.get_rows()):
            for col in range(self.get_cols()):
                y = row * self.get_state_height()
                x = col * self.get_state_width()
                ground = Ground(x, y)
                self.addBackground_first(ground)

    def verifica_caminho(self, inicio, destino, h = 1):
        self.mapAux = self.map.copy()
        #Substitui elementos no ambiente em que o agente pode passar para um mesmo valor
        self.mapAux[self.mapAux == 3] = -99
        self.mapAux[self.mapAux == 6] = -99
        return self.verifica_caminho_(self.mapAux, inicio, destino, h)

    def verifica_caminho_(self, mapa, origem, destino, h = 1, action = 0):    

        self.origem = origem        
        print("{}, {}".format(origem, destino))
        linha  = origem[0]
        coluna = origem[1]
                                                        

        if (linha == destino[0] and coluna == destino[1]) and mapa[linha][coluna] != -9: 
            
            #Calcula as coordenadas X, Y no ambiente para o agente se mover
            x = coluna * 16
            y = linha  * 16
            self.player.changeX = x
            self.player.changeY = y            

            mapa[linha][coluna] = h
            self.reached = True
            #atualiza e renderiza a tela do pygame    
            self.update()
            self.render()            
            #time.sleep(5)            
            return True

        action_map = {
            1 : 'left',
            2 : 'right',            
            3 : 'up',        
            4 : 'down',
            0 : 'no_op'
        }       
        print( "{} ".format(action_map[action]))        

        if mapa[linha][coluna] == 0 or mapa[linha][coluna] == -99:

            #Calcula as coordenadas X, Y no ambiente para o agente se mover
            x = coluna * 16
            y = linha  * 16
            self.player.changeX = x
            self.player.changeY = y

            #Marca a posição no mapa como visitado
            mapa[linha][coluna] = h

            #atualiza e renderiza a tela do pygame    
            self.update()
            self.render()

            #timer utilizar para controlar o tempo de espera do agente para realizar o próximo movimento
            time.sleep(self.tick_agent)            

            if (self.verifica_caminho_(mapa, (linha, max(0, coluna-1)), destino, h+1, action = 1)):
                return True
            
            if (self.verifica_caminho_(mapa, ( max(0, linha-1), coluna), destino, h+1, action = 3)):
                return True            
         
            if (self.verifica_caminho_(mapa, (linha, min(coluna+1, self.cols-1)), destino, h+1, action = 2)):
                return True               
            
            if (self.verifica_caminho_(mapa, ( min(linha+1, self.rows-1), coluna), destino, h+1, action = 4)):
                return True
        
        return False

    def border_offset(self):
        return (1, 1)

    def get_info(self):
        params = { }
        return params
        
    def do(self, event):
        super().do(event)
        if event.type == KEYDOWN:
            if event.key == K_F12:
                self.reset(self.np_random)
                    
    def step(self, entity):                                
        reward = 0.0                        
        return reward

    def reset(self, np_random = None):
        self.np_random = np_random
        self.clear_layers()
        self.generate_map(np_random)                
        self.update()                
    
    def get_tile_name(self, id):
        return self.tiles[id]

    def get_tiles(self):
        return self.tiles        

    def place_objects(self, obj_id, num_objs):
        tiles = [Ground.ID]
        map_locations = self.get_tile_positions(tiles, self.map)
        for j in range(num_objs):            
            index = self.np_random.randint(len(map_locations))            
            position = map_locations[index]
            row = position[0]
            col = position[1]

            while (self.map[row][col] == obj_id):
                index = self.np_random.randint(len(map_locations))
                position = map_locations[index]
                row = position[0]
                col = position[1]

            self.change_tile(col * self.get_state_width(), row * self.get_state_height(), obj_id)            
            
    
    def load_map(self, path_map):   
        data = []
        with open(path_map, newline='') as csvfile:
            data = list(csv.reader(csvfile))            
            
        data = np.array(data).astype("int") 
        
        self.map = data
        self.clear()        
        self.__create()
        
    def render_map(self):
        self.__create()
        self.render(tick=0)            
        
    def create_map(self, data):    
        self.map = data
        if not self.blocked:
            self.__create()  
            
    def update_map(self):
        self.clear()
        self.__create() 

    def generate_map(self, random = None):                  
        border = 0    
        
        if self.border:
            border = self.border_offset()[0] + self.border_offset()[1] 

        self.map = np.zeros((self.get_rows()-border, self.get_cols()-border))
        self.map = np.array(self.map).astype("int") 
        if self.border:
            self.map = fast_pad(self.map, 1)               
        self.__create()

    def change_tile(self, x, y, val):
        if not self.blocked:
            col = int(x / self.get_state_width())
            row = int(y / self.get_state_height())
            
            state_w = self.get_state_width()
            state_h = self.get_state_height()

            rect = pygame.Rect(x, y,  state_w, state_h)
            aux = pygame.sprite.Sprite()
            aux.image = pygame.Surface((state_w, state_h))
            aux.rect = rect

            collide = pygame.sprite.spritecollide(aux, self.bases, True)
            collide = pygame.sprite.spritecollide(aux, self.background, True)
            collide = pygame.sprite.spritecollide(aux, self.enemies, True)
            collide = pygame.sprite.spritecollide(aux, self.structure, True)
            collide = pygame.sprite.spritecollide(aux, self.levelObjects, True)
            collide = pygame.sprite.spritecollide(aux, self.players, True)
                    
            tile = self.create_tile(val, x = col * state_w, y = row * state_h)                         

            self.map[row, col] = tile     
    
    
    def create_tile(self, tile, x, y):        
        val = tile
        if val == Ground.ID:
            tile  = Ground(id = Ground.ID, x = x, y = y)                    
            self.addBackground(tile)                   
        elif val == Block.ID:
            tile  = Block(id =Block.ID, x = x, y = y)                    
            self.addBases(tile)                                            
        elif val == DoorEntrance.ID:
            tile  = DoorEntrance(id = DoorEntrance.ID, x = x, y = y)                    
            self.addBases(tile)
        elif val == DoorExit.ID:
            tile  = DoorExit(id = DoorExit.ID, x = x, y = y)                    
            self.addBases(tile)                   
        elif val == Coin.ID:
            tile  = Coin(id = Coin.ID, x = x, y = y)                    
            self.addLevelObjects(tile)                        
        elif val == Key.ID:
            tile  = Key(id = Key.ID, x = x, y = y)                    
            self.addLevelObjects(tile) 
        elif val == Player.ID:
            tile  = Player(id = Player.ID, x = x, y = y)                    
            self.addPlayers(tile)  
            self.player = tile
        elif val == Enemy.ID:
            tile  = Enemy(id = Enemy.ID, x = x, y = y)                    
            self.addEnemies(tile)            
        elif val == Weapon.ID:
            tile  = Weapon(id = Weapon.ID, x = x, y = y)                    
            self.addLevelObjects(tile)
        else:
            assert False, "unknown tile in decode '%s'" % tile

        return tile

    def __create(self):
        
        state_w = self.get_state_width()
        state_h = self.get_state_height()
        
        for row in range(self.get_rows()):
            for col in range(self.get_cols()):                
                val = self.map[row, col]
                tile = self.create_tile(val, x = col * state_w, y = row * state_h)

        super().create()

    def draw_hud(self, screen):
        if self.show_matriz:
            space_line    = 16
            current_line  = 0
            rowsize, colsize = self.mapAux.shape
            for r in range(rowsize):
                for c in range(colsize):
                    current_line += space_line        
                    text = str(self.mapAux[r][c])
                    self.draw_text_ext(x=c*16, y=r*16, text=text, color=Color(0,0,0), font=self.fntHUD)