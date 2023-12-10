import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
print(pygame.USEREVENT)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.draw.Surface(screen, (255,0,0), 50, 50)
    pygame.display.flip()

pygame.quit()
