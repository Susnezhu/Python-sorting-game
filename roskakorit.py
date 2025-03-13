import pygame
import random
 
from kuvien_lataus import *
 
 
class Roskakorit:
    def __init__(self, kuva, arvo, x, y):
        self.kuva = kuva
        self.arvo = arvo
        self.x = x
        self.y = y
 
        self.reunat = self.kuva.get_rect(topleft=(x, y))
 
    def lisaa(self, naytto):
        naytto.blit(self.kuva, (self.x,self.y))
 
 
 
roskakorit = [Roskakorit(bio_roskakori, 5, 700, 260),
              Roskakorit(kartonki_roskakori, 2, 500, 260),
              Roskakorit(lasi_roskakori, 4, 100, 200),
              Roskakorit(metalli_roskakori, 6, 300, 200),
              Roskakorit(muovi_roskakori, 3, 600, 270),
              Roskakorit(paperi_roskakori, 1, 200, 200)]


 