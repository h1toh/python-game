import pygame
import pygame.ftfont
from pygame.locals import *
from sys import exit
from random import random

pygame.init()
# Iniciar o pygame

pygame.mixer.init()
pygame.mixer.music.load('audios/ost_theme.mp3')
pygame.mixer.music.play(-1)
#  Tocar OST em looping

fps = 45
relogio = pygame.time.Clock()
#  Quadros por segundo

tela_largura = 1080
tela_altura = 720
tela = pygame.display.set_mode((tela_largura, tela_altura))
# Definindo b:h da Tela

pygame.display.set_caption('The Square')
# Título do Jogo

fonte = pygame.font.SysFont('arial', 25, True, False)
# Fonte de texto principal do jogo

obj_largura = 100
obj_altura = 100
o_x = tela_largura/2 - obj_largura/2
o_y = 0 - obj_altura
obj_velocidade = 7
# Objeto que mata o Player

player_largura = 50
player_altura = 50
p_x = 30
p_y = tela_altura / 2 - player_altura / 2
p_velocidade_inicial = 14
p_velocidade = p_velocidade_inicial
# Player

comida_largura = 15
comida_altura = 15
comida_x = tela_largura * random() - comida_largura
comida_y = tela_altura * random() - comida_altura
comida_sfx = pygame.mixer.Sound('audios/sfx/sfx_food.wav')
# Comida

pontos = 0
# Pontuaçãi inicial

while True:
    relogio.tick(fps)
    tela.fill((0,0,0))
    # Cor do background

    texto_pontos = f'Score: {pontos}'
    texto_pontos_formatado = fonte.render(texto_pontos, True, (255,255,255))
    # Texto com pontuação do player


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
    # Sair do jogo

    rect_comida = pygame.draw.rect(tela, (255,255,0), (comida_x, comida_y, comida_largura, comida_altura))
    # Criação da Comida

    rect_player = pygame.draw.rect(tela, (0,255,0), (p_x, p_y, player_largura, player_altura))
    if pygame.key.get_pressed()[K_a] and p_x > 0: 
        p_x -= p_velocidade
    if pygame.key.get_pressed()[K_d] and p_x < tela_largura - player_largura:
        p_x += p_velocidade
    if pygame.key.get_pressed()[K_w] and p_y > 0:
        p_y -= p_velocidade
    if pygame.key.get_pressed()[K_s] and p_y < tela_altura - player_altura:
        p_y += p_velocidade
    # Criação do Player

    rect_obj = pygame.draw.rect(tela, (255,0,0), (o_x, o_y, obj_largura, obj_altura))
    o_y += obj_velocidade
    if o_y > tela_altura + obj_altura:
        o_y = 0 - obj_altura
    # Criação do Objeto

    if rect_player.colliderect(rect_obj):
        p_x = 30
        p_y = tela_altura / 2 - player_altura / 2
        comida_x = tela_largura * random()
        comida_y = tela_altura * random()
        obj_velocidade = 7
        o_y = 0 - obj_altura
        pontos = 0
        p_velocidade = p_velocidade_inicial
    # Quando Player colide com Objeto

    if rect_player.colliderect(rect_comida):
        comida_sfx.play()
        pontos += 1
        comida_x = tela_largura * random()
        comida_y = tela_altura * random()
        obj_velocidade += 1
    # Quando Player colide com a Comida
            


    tela.blit(texto_pontos_formatado, (tela_largura - tela_largura/4, 40))
    # Colocando texto(pontuação) na tela

    pygame.display.update()
    # Sempre atualizando o jogo
