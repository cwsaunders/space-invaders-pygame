import pygame
import random


def player(img,x,y):
    window.blit(img,(x,y))

def enemy(img,x,y):
    window.blit(img,(x,y))

pygame.init()

# Creates game window
window = pygame.display.set_mode((800,600))

# Aesthetic choices
# Description
pygame.display.set_caption("Space Invaders")
# Icon
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
# Enemy:
enemyImg = pygame.image.load('skull.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0


# Game loop
running = True
while running:
    # Background: (RGB)
    window.fill((0, 255, 255))

    # Event check and execute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Player:
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerImg,playerX,playerY)

    # Enemy:
    enemy(enemyImg,enemyX,enemyY)

    # Update original background
    pygame.display.update()

