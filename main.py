from structs import *
import pygame


width, height = 1280, 720

pygame.init()

window = pygame.display.set_mode((width, height))
player = Player()

group_sprites.add(player)
group_sprites.add(levelMap)

inGame = True
background = pygame.image.load('images/testback.png')

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock = pygame.time.Clock()
    # pygame.mouse.set_visible(False) пока так потом кастом курсор
    # window.blit(background, (0, 0))  # фон
    key = pygame.key.get_pressed()

    if inGame:
        window.fill((100, 100, 100))

        if key[pygame.K_m]:
            print('Cords=', (player.x, player.y), ' <impulse=', player.impulse, "> <collide=", "> <", sep="", end=">\n")

        if key[pygame.K_d]:  # движение героя
            player.move_right()
        if key[pygame.K_a]:
            player.move_left()
        if key[pygame.K_SPACE]:
            player.jump()
        if key[pygame.K_f]:
            player.impulse = 0
            player.y -= 2

        group_sprites.draw(window)
        group_sprites.update()

    pygame.display.update()
    clock.tick(200)

pygame.quit()
