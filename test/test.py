import pygame


# class Circle(pygame.sprite.Sprite):
class Circle():
    def __init__(self, pos, color, radius, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))  # Create 1 32x32 Surface instance Image
        self.image.set_colorkey((1, 2, 3))  # Set the color of the color (1,2,3) in the IMAGE is transparent
        self.image.fill((1, 2,
                         3))  # The background color is black, due to the upper strip, the background color becomes transparent
        self.radius = radius
        self.width = width
        pygame.draw.circle(self.image, pygame.Color(color), (50, 50), self.radius,
                           self.width)  # Draw round on the image
        self.rect = self.image.get_rect(
            center=pos)  # Rect define the IMAGE boundary and position, and move the image to the specified location
        self.mask = pygame.mask.from_surface(self.image)  # Create records transparent and opaque points MASK

    def draw(self, aSurface):
        aSurface.blit(self.image,
                      self.rect)  # Sprite derived category instances are not put in group, and the class instance shows that you need to call a custom DRAW


pygame.init()
screen = pygame.display.set_mode((200, 100))
pygame.display.set_caption("Circle and ring collision")
clock = pygame.time.Clock()
circleRed = Circle((50, 50), 'red', 45, 10)  # Create a red circle instance as a ring
circleblue = Circle((150, 50), 'blue', 15, 0)  # Create a red circle instance as a solid circle
run = True
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # Press the event after the key
            if event.key == pygame.K_RIGHT:  # to the right
                circleblue.rect.x += 5
            elif event.key == pygame.K_LEFT:  #
                circleblue.rect.x -= 5
                # if pygame.sprite.collide_mask(circleblue,circleRed):
    offset = circleRed.rect.x - circleblue.rect.x, circleRed.rect.y - circleblue.rect.y  # Cannot be exchanged
    if circleblue.mask.overlap(circleRed.mask, offset) != None:
        screen.fill((200, 200, 200))
    else:
        screen.fill((255, 255, 255))
    circleRed.draw(screen)
    circleblue.draw(screen)
    clock.tick(10)
    pygame.display.update()
pygame.quit()