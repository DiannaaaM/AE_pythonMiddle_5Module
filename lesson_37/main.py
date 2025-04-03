import random
import pygame
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Вектор для удобного управления позициями
vec = pygame.math.Vector2

# Определяем константы
ACC = 0.5  # Ускорение
FRIC = -0.12  # Трение
WIDTH, HEIGHT = 800, 600  # Размеры экрана

# Настройка окна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движение игрока')

# Класс Player для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))  # Цвет игрока (зеленый)
        self.rect = self.surf.get_rect()
        self.pos = vec((10, HEIGHT - 35))  # Начальная позиция, над платформой
        self.vel = vec(0, 0)  # Начальная скорость
        self.acc = vec(0, 0)  # Начальное ускорение

    def move(self):
        self.acc = vec(0, 0.5)  # Добавляем гравитацию

        pressed_keys = pygame.key.get_pressed()

        # Управление влево
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        # Управление вправо
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        # Учитываем трение для замедления
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Уравнение движения

        # Реализация "screen warping" - если игрок выходит за экран
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        # Проверка на столкновение с платформой
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1  # Устанавливаем позицию игрока над платформой
            self.vel.y = 0  # Обнуляем вертикальную скорость

# Класс Platform для платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 0))  # Цвет платформы (зеленый)
        self.rect = self.surf.get_rect()

# Создаем группы спрайтов для платформ
platforms = pygame.sprite.Group()  # Группа платформ

# Создаем неподвижную нижнюю платформу
bottom_platform = Platform(WIDTH, 20)
bottom_platform.rect.center = (WIDTH / 2, HEIGHT - 10)
platforms.add(bottom_platform)

# Создаем дополнительные платформы
def plat_gen():
    while len(platforms) < 7:  # Ограничим количество динамических платформ
        width = random.randrange(50, 100)
        p = Platform(width, 12)
        p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(0, HEIGHT - 30))
        platforms.add(p)

plat_gen()  # Генерируем дополнительные платформы

# Создаем игрока
P1 = Player()

# Группа всех спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(platforms)

# Главный игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление состояния игры
    P1.move()  # Обновляем движение игрока
    P1.update()  # Обновляем состояние игрока

    # Отображение
    window.fill((0, 0, 0))  # Очистка экрана
    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)

    pygame.display.update()  # Обновление экрана

    # Ограничение FPS
    clock.tick(60)

# Завершаем работу Pygame
pygame.quit()
