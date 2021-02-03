import pygame
import sys
import random

pygame.init()

W = 400
H = 600
stage = 1
Fps = 140

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load('tex/bird.png')
        self.image = self.image_orig
        self.image_rect = self.image.get_rect(center=(100, 300))
        self.going_up = False

    def update(self):
        global stage
        if not self.going_up:
            self.image_rect.y = self.image_rect.y + 2
        if self.image_rect.bottom < 0 or self.image_rect.bottom > 480:
            stage = 2

    def jump(self):
        if stage == 1:
            self.going_up = True
            self.image_rect.y -= 100
            self.going_up = False


class Tubes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tex/bg.png')
        self.image_rect = self.image.get_rect(topleft=(0, 0))
        self.go_image = pygame.image.load('tex/go_bg.png')
        self.go_image_rect = self.image.get_rect(topleft=(0, 0))

    def update(self):
        if stage == 1:
            self.image_rect.x -= 1
        if self.image_rect.x == -400:
            self.image_rect.x = 0


bird = Bird()
bg = Bg()


def mainloop():
    global stage
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)
            if event.key == pygame.K_SPACE:
                if stage == 1:
                    bird.jump()
                if stage == 2:
                    bird.image_rect.y = 100
                    stage = 1
    if stage == 1:
        screen.blit(bg.image, bg.image_rect)
        screen.blit(bird.image, bird.image_rect)
        bg.update()
        bird.update()
    if stage == 2:
        screen.blit(bg.go_image, bg.go_image_rect)
    clock.tick(Fps)
    pygame.display.flip()


while True:
    mainloop()
