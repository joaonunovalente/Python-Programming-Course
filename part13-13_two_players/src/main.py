import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")
x1 = 540 - robot1.get_width()
y1 = 240 - robot1.get_height()
x2 = 100
y2 = 240 - robot2.get_height()

to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

to_right2 = False
to_left2 = False
to_up2 = False
to_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_DOWN:
                to_down1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_UP:
                to_up1 = False
            if event.key == pygame.K_DOWN:
                to_down1 = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                to_up2 = True
            if event.key == pygame.K_s:
                to_down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                to_up2 = False
            if event.key == pygame.K_s:
                to_down2 = False

        if event.type == pygame.QUIT:
            exit()

    if to_right1 and x1 < 640 - robot1.get_width():
        x1 += 2
    if to_left1 and x1 > 0:
        x1 -= 2
    if to_up1 and y1 > 0:
        y1 -= 2
    if to_down1 and y1 < 480 - robot1.get_height():
        y1 += 2

    if to_right2 and x2 < 640 - robot2.get_width():
        x2 += 2
    if to_left2 and x2 > 0:
        x2 -= 2
    if to_up2 and y2 > 0:
        y2 -= 2
    if to_down2 and y2 < 480 - robot2.get_height():
        y2 += 2             

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    clock.tick(60)