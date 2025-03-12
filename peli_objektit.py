import pygame
import random

from kuvien_lataus import *

class PeliObjektit:
    def __init__(self, kuva, arvo):
        self.x = random.randint(0, 900 - kuva.get_width())
        self.y = random.randint(350, 600-65)
        
        self.kuva = kuva
        self.reunat = self.kuva.get_rect(topleft=(self.x, self.y))
        
        self.arvo = arvo
        
    def paivita(self, dx, dy):
        self.reunat.x += dx
        self.reunat.y += dy

    def lisaa(self, screen):
        screen.blit(self.kuva, self.reunat.topleft)
    

#lista, jossa on PeliObjekti luokan oliot
objektit = (
    [PeliObjektit(roska, 1) for roska in paperi] + 
    [PeliObjektit(roska, 2) for roska in kartonki] + 
    [PeliObjektit(roska, 3) for roska in muovi] + 
    [PeliObjektit(roska, 4) for roska in lasi] + 
    [PeliObjektit(roska, 5) for roska in bio] + 
    [PeliObjektit(roska, 6) for roska in metalli]
)

