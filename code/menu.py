#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_LIGHT_GREEN, COLOR_PURPLE, MENU_OPTION, COLOR_WHITE, COLOR_SKY_BLUE, \
    COLOR_NEON_RED, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window

        # Trazendo imagem para projeto e salvando no objeto surf:

        self.surf = pygame.image.load('./asset/menuBg.png')

        # Criando um objeto( rect) e utilizando o objeto com a imagem
        # para fazer um retangulo onde a imagem ficara passando parametros(left,top)

        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):

        #  A variavel menu_option recebeu valor pois esta e a posicao da primeira opcao
        #  do menu (new game). Olhar linha 53
        menu_option = 0
        # Adicionando musica de fundo com o pygame.mixer_music.load
        # Lembrando que aqui a musica somente foi carregada
        pygame.mixer_music.load('./asset/menu_music.mp3')

        # Reproduzindo a musica indefinidamente (parametro -')
        pygame.mixer_music.play(-1)

        while True:

            # Depois de criar a imagem e preciso desenha-la para poder
            # usar a janela. E para isso se usa o metodo blit()

            self.window.blit(source=self.surf, dest=self.rect)

            # Escrevendo texto na janela
            # Lembrar sempre de manter a ordem primeiro precisa desenhar o fundo (linha 41),
            # para depois mostrar o texto na tela(linha 46)

            self.menu_text(60, "City", COLOR_SKY_BLUE, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, "Shooter", COLOR_NEON_RED, ((WIN_WIDTH / 2), 130))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 26 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 26 * i))
            pygame.display.flip()

            # Mesmo apos isso tudo e preciso usar um metodo para poder atualizar a tela
            # utilizando o metodo pygame.diaplay.flip

            # ob : se a imagem nao estiver do tamanho certo da janela(muito provavel),
            # lembrar de mudar o tamanho da janela ou redimensionar a imagem para o
            # tamanho da janela.

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

                #  Navegando pelo menu com a tecla S
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    #  Navegando pelo menu com a tecla W
                    if event.key == pygame.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # Configurando tecla enter para selecao de opcao do menu
                    if event.key == pygame.K_RETURN:
                       return  MENU_OPTION[menu_option]

                #  Navegando pelo menu com a tecla W

            

    # Metodo para criar  texto do menu
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)




