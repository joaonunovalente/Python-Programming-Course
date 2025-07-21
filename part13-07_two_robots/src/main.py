import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x1 = 0
x2 = 0
y = 0
clock = pygame.time.Clock()

pygame.display.flip()

velocity_x1 = 1
velocity_x2 = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y + 100))
    window.blit(robot1, (x2, y + 200))
    pygame.display.flip()

    x1 += velocity_x1
    x2 += velocity_x2

    if velocity_x1 > 0 and x1 + robot1.get_width() >= 640:
        velocity_x1 = -velocity_x1
    elif velocity_x1 < 0 and x1 <= 0:
        velocity_x1 = -velocity_x1
    
    if velocity_x2 > 0 and x2 + robot2.get_width() >= 640:
        velocity_x2 = -velocity_x2
    elif velocity_x2 < 0 and x2 <= 0:
        velocity_x2 = -velocity_x2

        
    clock.tick(60)