import pygame
import random

from kuvien_lataus import *

class PeliObjektit:
    def __init__(self, kuva, arvo):
        self.x = random.randint(0, 900 - kuva.get_width())
        self.y = random.randint(450, 600 - kuva.get_height())
        
        self.kuva = kuva
        self.reunat = self.kuva.get_rect(topleft=(self.x, self.y))
        
        self.arvo = arvo
        self.alkuperaiset_kordinaatit = self.x, self.y
        
    def paivita(self, x, y):
        self.reunat.topleft = (x - self.kuva.get_width()/2, y - self.kuva.get_height()/2)
 
    def lisaa(self, screen):
        screen.blit(self.kuva, self.reunat.topleft)
 
    def siirry(self, x, y):
        if self.reunat.collidepoint(x, y):
            self.paivita(x, y)

    def poista(self, lista):
        if self in lista:
            lista.remove(self)
    
    def kopio(self):
        uusi_objekti = PeliObjektit(self.kuva.copy(), self.arvo)
        uusi_objekti.x, uusi_objekti.y = self.alkuperaiset_kordinaatit
        uusi_objekti.reunat = uusi_objekti.kuva.get_rect(topleft=(uusi_objekti.x, uusi_objekti.y))
        return uusi_objekti
            
#lista, jossa on PeliObjekti luokan oliot
objektit = (
    [PeliObjektit(roska, 1) for roska in paperi] +
    [PeliObjektit(roska, 2) for roska in kartonki] +
    [PeliObjektit(roska, 3) for roska in muovi] +
    [PeliObjektit(roska, 4) for roska in lasi] +
    [PeliObjektit(roska, 5) for roska in bio] +
    [PeliObjektit(roska, 6) for roska in metalli]
)
objektit_kopio = (
    [PeliObjektit(roska, 1) for roska in paperi] +
    [PeliObjektit(roska, 2) for roska in kartonki] +
    [PeliObjektit(roska, 3) for roska in muovi] +
    [PeliObjektit(roska, 4) for roska in lasi] +
    [PeliObjektit(roska, 5) for roska in bio] +
    [PeliObjektit(roska, 6) for roska in metalli]
)
