#Pelin koodi kirjoitetaan tähän
import pygame

pygame.init()

from kuvien_lataus import * #tiedosto, jossa on kaikki kuvat
from peli_objektit import * #tiedosto, jossa on luokka PeliObjektit

LEVEYS = 900
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Roskien lajittelu peli")



while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = tapahtuma.pos
            for obj in objektit:
                if obj.reunat.collidepoint(x, y):
                    print("object found") #tähän pitää lisätä hiiren seuraaminen
                    print(obj.arvo) #kertoo mihin roskikseen se menee


        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.blit(taustakuva, (0,0))
    for objekti in objektit:
        objekti.lisaa(naytto)
    

    pygame.display.flip()