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

velocity_x = 2
velocity_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity_x
    y += velocity_y

    if velocity_x > 0 and x + robot_width >= 640:
        x = 640 - robot_width
        velocity_x, velocity_y = 0, 2
    elif velocity_y > 0 and y + robot_height >= 480:
        y = 480 - robot_height
        velocity_x, velocity_y = -2, 0
    elif velocity_x < 0 and x <= 0:
        x = 0
        velocity_x, velocity_y = 0, -2
    elif velocity_y < 0 and y <= 0:
        y = 0
        velocity_x, velocity_y = 2, 0
        
    clock.tick(60)