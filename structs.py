import pygame
import os
import random


def load_image(name):
    """
    Функция загрузки изображения из файла.
    :param name: Имя файла
    :return: изображение
    """
    filename = os.path.join('images', name)
    try:
        image = pygame.image.load(filename)
    except pygame.error as error:
        print('Не могу загрузить изображение:', name)
        raise SystemExit(error)
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(group_sprites)
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.first = ""
        self.second = ""
        self.third = ""
        self.images = list()  # all images

        self.image = pygame.transform.scale(load_image("bopl.png"), (35, 35))
        """for i in range(1):
            self.images.append()"""
        self.images = [self.image]
        # self.image_slicer()
        self.rect = self.image.get_rect(center=(self.image.get_width()/2+self.x,self.image.get_height()/2+self.y))
        self.mask = pygame.mask.from_surface(self.image)

        self.right = True
        self.impulse = 0

    def image_slicer(self):
        pass

    def update(self):
        self.x = int(self.x)
        self.y = int(self.y)
        self.image = self.images[0]  # заглушка
        self.image = self.image if self.right else pygame.transform.flip(self.image, True, False)
        self.rect.center = self.x, self.y  # хз че это с ней работает
        self.gravitation()
        # image = self.images[(abs(self.timer // (500 // 4)) - 1) % 4]   поменять
        # self.image = image if self.right else pygame.transform.flip(image, True, False)

    def move_right(self):
        self.x += 2
        self.rect.center = self.x, self.y
        self.right = True

    def move_left(self):
        self.x -= 2
        self.rect.center = self.x, self.y
        self.right = False

    def jump(self):
        if self.in_surface():
            self.y -= 3
            self.rect.center = self.x, self.y
            self.impulse = 6

    def in_surface(self):
        """offset = self.rect.x - levelMap.rect.x, self.rect.y - levelMap.rect.y
        if self.mask.overlap(levelMap.mask, offset) is not None:
            self.impulse = 0
            return True

        if pygame.sprite.collide_mask(self, levelMap):
            self.impulse = 0
            return True
        # проверка на то находится ли бопл на земле"""

        return any([pygame.sprite.collide_mask(self, i) is not None for i in levelMap])

    def gravitation(self):
        if not self.in_surface():
            self.y += (1 - self.impulse)
            self.rect.move(0, 1 - self.impulse)
            if self.impulse != 0:
                self.impulse -= 0.1
        else:
            self.impulse = 0

    def attack(self, n):
        pass


class Weapon:
    pass


class Map(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.image.get_width()/2+self.x,self.image.get_height()/2+self.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.move(x, y)


"Map(pygame.image.load('images/testback.png'), 0, 360)"

levelMap = [Map(pygame.transform.scale(load_image('block1.png'), (136, 81)), random.randint(0, 1200), random.randint(0, 720))
            for _ in range(10)]
group_sprites = pygame.sprite.Group()
