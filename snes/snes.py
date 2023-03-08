import pygame

pygame.init()

clk = pygame.time.Clock()
#a ver si se sube el commit
size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('./templates/control.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
crosshairz = pygame.surface.Surface((256,256),pygame.SRCALPHA, 32)
crosshairx = pygame.surface.Surface((256,256),pygame.SRCALPHA, 32)
crosshairc = pygame.surface.Surface((256,256),pygame.SRCALPHA, 32)
crosshairv = pygame.surface.Surface((256,256),pygame.SRCALPHA, 32)
pygame.draw.circle(crosshair, pygame.Color("blue"), (8, 8), 8, 0)
pygame.draw.circle(crosshairz, pygame.Color("yellow"), (8, 8), 8, 0)
pygame.draw.circle(crosshairx, pygame.Color("blue"), (8,8), 8, 0)
pygame.draw.circle(crosshairc, pygame.Color("green"), (8,8), 8, 0)
pygame.draw.circle(crosshairv, pygame.Color("red"), (8,8), 8, 0)


crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)




while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))

    Keys=pygame.key.get_pressed()

    if Keys[pygame.K_x]: screen.blit(crosshairx, (193.5, 100.5))
    if Keys[pygame.K_c]: screen.blit(crosshairc, (169, 120))
    if Keys[pygame.K_v]: screen.blit(crosshairv, (218, 120))
    if Keys[pygame.K_z]: screen.blit(crosshairz, (193.6, 139.5))

    if Keys[pygame.K_KP_ENTER]: screen.blit(crosshair, (100, 60))
    if Keys[pygame.K_l]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_j]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_i]: screen.blit(crosshair, (200, 100))

    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*20)+55-5, (y*20)+125-5))

    pygame.display.flip()

    clk.tick(40)