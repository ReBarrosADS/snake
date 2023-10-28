import pygame   
import random

pygame.init()
pygame.display.set_caption("Jogo snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

## Definindo as cores

preta = (0, 0, 0)
branca = (255,255,255)
vermelho = (255, 0, 0)
verde = (0,255, 0)

## quadrado para localizar a cobrinha
tamanho_quadrado = 20

##entre loop a cobra vai andar 15
velocidade_jogo = 15

def gerar_comida():

    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20) * 20.0
    comida_y = round(random.randranger(0, altura - tamanho_quadrado) / 20) * 20.0

    return comida_x, comida_y
def desenhar_comida(tamanho, comida_x, comida_y):

    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel [1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35) 
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    
def rodar_jogo():
    fim_jogo = False

    x = largura / 2

    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1

    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = true
        # desenhar comida
        desenhar_comida(tamanho, comida_x, comida_y)
        

        #desenhar cobra
        pixels.appned([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #se a cobra bater no propio corpo
        for pixel in pixels:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho, pixels)
        desenhar_pontuacao(tamanho)

        # atualização de tela
        pygame.display.update()






