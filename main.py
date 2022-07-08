import pygame
pygame.init()

screenHeight = 500
screenWidth = 500

window = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Test Game")

walking = [pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk00.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk01.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk02.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk03.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk04.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk05.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk06.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk07.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk08.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk09.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk10.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/walk11.png")]
standing = [pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle00.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle01.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle02.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle03.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle04.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle05.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle06.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle07.png"), pygame.image.load("Graphics/Atlases/Gameplay/characters/player/idle08.png")]
bg = pygame.image.load("Graphics/Atlases/MirrorTemple/00.png")

x = 50
y = 425
width = 32
height = 32
velocity = 5
isJump = False
jumpCount = 10
left = False
right = True
walkCount = 0
idleCount = 0


def redraw_game_window():
    global walkCount
    global idleCount

    window.blit(bg, (0, 0))

    if walkCount + 1 >= 36:
        walkCount = 0

    if idleCount + 1 >= 27:
        idleCount = 0

    if left:
        window.blit((pygame.transform.flip(walking[walkCount // 3], True, False)), (x, y))
        walkCount += 1
    elif right:
        window.blit(walking[walkCount // 3], (x, y))
        walkCount += 1
    else:
        window.blit(standing[idleCount // 3], (x, y))
        idleCount += 1

    pygame.display.update()


running = True
while running:
    pygame.time.delay(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_d] and x < screenWidth - width:
        x += velocity
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraw_game_window()

pygame.quit()
