import pygame, sys

from pygame.locals import QUIT

GRAY = (100, 100, 100)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 275))

class Platform:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, GRAY, self.rect)


WINDOW_WIDTH = 400 # в этой переменной будем хранить шириниу создаваемого окна
WINDOW_HEIGHT = 300 # в этой переменной будем хранить высоту создаваемого окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Platformer')

NEON_BLUE = (173, 216, 230)
clock = pygame.time.Clock()
FPS = 30
P1 = Player()
platform = Platform(400, 10, 0, 290)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))
    platform.draw(window)

    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)

    pygame.display.update()
    clock.tick(FPS)