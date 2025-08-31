import math
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

angle = 0
clock = pygame.time.Clock()

pygame.display.flip()

velocity_x = 2
velocity_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0, 0, 0))
    ### Formula
    # x = center_x + cos(angle + offset) * radius - half_width
    # y = center_y + sin(angle + offset) * radius - half_height
    # offset = 2π * i / number = 2π * i / 10 = π * i / 5
    for i in range(0,10):
        x = 320+math.cos(angle + i * math.pi/5)*100-robot.get_width()/2
        y = 240+math.sin(angle + i * math.pi/5)*100-robot.get_height()/2
        window.blit(robot, (x, y))
    pygame.display.flip()
    angle += 0.01

        
    clock.tick(60)