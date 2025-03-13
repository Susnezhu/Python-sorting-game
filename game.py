#Pelin koodi kirjoitetaan tähän
import pygame

pygame.init()

from kuvien_lataus import * #tiedosto, jossa on kaikki kuvat
from peli_objektit import * #tiedosto, jossa on luokka PeliObjektit
from roskakorit import *

LEVEYS = 900
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Roskien lajittelu peli")


seuraa_hiirta = False
valittu_objekti = None
while True:
    naytto.blit(taustakuva, (0,0))
    
    for roskakori in roskakorit:
        roskakori.lisaa(naytto)
 
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = tapahtuma.pos
            for obj in reversed(objektit):
                if obj.reunat.collidepoint(x, y):
                    seuraa_hiirta = True
                    valittu_objekti = obj
                    break
        if tapahtuma.type == pygame.MOUSEBUTTONUP:
            seuraa_hiirta = False
            valittu_objekti = None
 
        if tapahtuma.type == pygame.MOUSEMOTION and seuraa_hiirta:
            x,y = tapahtuma.pos
            if valittu_objekti:
                valittu_objekti.siirry(x, y)
 
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    for objekti in objektit:
        objekti.lisaa(naytto)
 
    pygame.display.flip()