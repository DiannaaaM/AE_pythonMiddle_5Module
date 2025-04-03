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
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Движение игрока')

# Класс Player для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))  # Цвет игрока (зеленый)
        self.rect = self.surf.get_rect()
        self.pos = vec((10, HEIGHT-15))  # Начальная позиция
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
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))  # Платформа по ширине всего экрана
        self.surf.fill((255, 0, 0))  # Цвет платформы (красный)
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))  # Центрируем платформу

# Создаем группы спрайтов для игрока и платформ
P1 = Player()
platform = Platform()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(platform)

platforms = pygame.sprite.Group()  # Группа платформ
platforms.add(platform)

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
    displaysurface.fill((0, 0, 0))  # Очистка экрана
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()  # Обновление экрана

    # Ограничение FPS
    clock.tick(60)

# Завершаем работу Pygame
pygame.quit()
