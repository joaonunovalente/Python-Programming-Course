import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

x = 0
y = 0
clock = pygame.time.Clock()

pygame.display.flip()

velocity = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += velocity
    if velocity > 0 and y + robot.get_height() >= 480:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity
    clock.tick(60)