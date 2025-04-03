import pygame, sys
from pygame.locals import QUIT

WINDOW_WIDTH = 400 # в этой переменной будем хранить шириниу создаваемого окна
WINDOW_HEIGHT = 300 # в этой переменной будем хранить высоту создаваемого окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Это шаблон')

NEON_BLUE = (173, 216, 230)
clock = pygame.time.Clock()
FPS = 30
# Бесконечный цикл для отображения окна и обработки событий
while True:
    # Заливка окна нежно синим цветом
    window.fill(NEON_BLUE)

    # Обработка событий pygame
    for event in pygame.event.get():
        # Если событие - выход из программы
        if event.type == QUIT:
            pygame.quit()  # Завершение работы pygame
            sys.exit()  # Завершение программы

    # Ограничение FPS
    clock.tick(FPS)

    pygame.display.update()  # Обновление содержимого окна