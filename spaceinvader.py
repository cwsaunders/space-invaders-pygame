import pygame
import random
import math
from pygame import mixer


def player(img,x,y):
    window.blit(img,(x,y))

def enemy(img,x,y):
    window.blit(img,(x,y))

def fire_bullet(img,x,y):
    global bullet_state
    bullet_state = 'fire'
    window.blit(img,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

def show_score(x,y):
    score = font.render(f"Score: {str(score_value)}",True, (255,255,255))
    window.blit(score, (x, y))

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
# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
# Enemy:
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('skull.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)
# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
# Ready - you cannot see bullet on screen
# Fire - bullet is moving
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

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
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        # Checking for boundaries of enemy
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

                # Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        # Enemy function
        enemy(enemyImg[i],enemyX[i],enemyY[i])


    # Bullet:
    # Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletImg,bulletX,bulletY)
        bulletY -= bulletY_change
    show_score(textX,textY)






    # Update original background
    pygame.display.update()
