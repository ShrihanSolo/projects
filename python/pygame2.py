import pygame
import time
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(width + 20 , width + 100),
                random.randint(0, height),
            )
        )
        self.speed = random.randint(0,4)/2

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Variable to keep the main loop running
running = True

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 125)

screen.fill((255,255,255))

surf = pygame.Surface((50,50))
surf.fill((0,255,255))
rect = surf.get_rect()
surfPosn = ((width-(surf.get_width()))/2, (height-(surf.get_height()))/2)
clock = pygame.time.Clock()

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Main loop
while running == True:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    screen.fill((0,0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False
    pygame.display.flip()
