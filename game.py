#Pelin koodi kirjoitetaan tähän
import pygame
 
pygame.init()
 
from kuvien_lataus import * #tiedosto, jossa on kaikki kuvat
from peli_objektit import * #tiedosto, jossa on luokka PeliObjektit
from roskakorit import * #tiedosto, jossa on luokka Roskakorit
 
LEVEYS = 900
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Roskien lajittelu peli")
 
 
pisteet = 0
 
peli_loppui = False
 
def uusi_peli():
    global peli_loppui, objektit, objektit_kopio, pisteet
    peli_loppui = False
    objektit = objektit_kopio
    pisteet = 0
 
 
seuraa_hiirta = False
valittu_objekti = None
while True:
    naytto.blit(taustakuva, (0,0))
 
    for roskakori in roskakorit:
        roskakori.lisaa(naytto)
 
    if objektit == []:
        peli_loppui = True
 
 
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
                if peli_loppui and tapahtuma.key == pygame.K_r:
                    uusi_peli()
        if not peli_loppui:
            if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
                x, y = tapahtuma.pos
                for obj in reversed(objektit):
                    if obj.reunat.collidepoint(x, y):
                        seuraa_hiirta = True
                        valittu_objekti = obj
                        break
            if tapahtuma.type == pygame.MOUSEBUTTONUP:
                seuraa_hiirta = False
                if valittu_objekti == None:
                    break
                for roska in roskakorit:
                    if roska.reunat.collidepoint(valittu_objekti.reunat.x, valittu_objekti.reunat.y):
                            valittu_objekti.poista(objektit)
                            if valittu_objekti.arvo == roska.arvo:
                                pisteet += 1
 
 
                valittu_objekti = None
    
            if tapahtuma.type == pygame.MOUSEMOTION and seuraa_hiirta:
                x,y = tapahtuma.pos
                if valittu_objekti:
                    valittu_objekti.siirry(x, y)
    
        if tapahtuma.type == pygame.QUIT:
            exit()
 
 
 
    if not peli_loppui:
        for objekti in objektit:
            objekti.lisaa(naytto)
    
        pygame.display.flip()