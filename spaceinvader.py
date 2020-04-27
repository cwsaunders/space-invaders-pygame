import pygame
import random


def player(img,x,y):
    window.blit(img,(x,y))

def enemy(img,x,y):
    window.blit(img,(x,y))

def fire_bullet(img,x,y):
    global bullet_state
    bullet_state = 'fire'
    window.blit(img,(x+16,y+10))


pygame.init()

# Creates game window
window = pygame.display.set_mode((800,600))

# Aesthetic choices
# Description
pygame.display.set_caption("Space Invaders")
# Icon
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
# Background
background = pygame.image.load('space background.jpg')

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
# Enemy:
enemyImg = pygame.image.load('skull.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 2
enemyY_change = 40
# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
# Ready - you cannot see bullet on screen
# Fire - bullet is moving
bullet_state = 'ready'


# Game loop
running = True
while running:
    # Background: (RGB)
    window.fill((0, 255, 255))
    # Background image
    window.blit(background, (0,0))
    # Event check and execute
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletImg,bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Player:
    # Movement
    playerX += playerX_change

    # Checking for boundaries of player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Player function
    player(playerImg,playerX,playerY)

    # Enemy:
    # Movement
    enemyX += enemyX_change

    # Checking for boundaries of enemy
    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change
    # Enemy function
    enemy(enemyImg,enemyX,enemyY)

    # Bullet:
    # Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletImg,bulletX,bulletY)
        bulletY -= bulletY_change

    # Update original background
    pygame.display.update()
