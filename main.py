#  Primeiros conceitos: git,github,intalacao e funcionamento do pygame

import pygame

print('setup start')

pygame.init()
x = 600
y = 800
window = pygame.display.set_mode(size=(y, x))

print('setup end')

print('loop start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame


# Aula pratica 2
# Diagramacao UMl do jogo
# Estruturar as classes
# Criar o menu
# Criar o background,som e fontes da priemria fase



