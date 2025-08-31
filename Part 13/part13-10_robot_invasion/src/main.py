from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
number_of_robots = 20
robots = [robot for _ in range(number_of_robots)]
position = [(randint(0 + robot.get_width(), 640 - robot.get_width()), randint(-1000,0)) for _ in range(number_of_robots)]

clock = pygame.time.Clock()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for i in range(number_of_robots):
        if position[i][1] + robot.get_height() >= 480:
            if position[i][0] >= 640 / 2:
                velocity_x = 2
                velocity_y = 0
            else:
                velocity_x = -2
                velocity_y = 0
        else:
            velocity_x = 0
            velocity_y = 2
        position[i] = (position[i][0] + velocity_x, position[i][1] + velocity_y)
        window.blit(robots[i], position[i])

    pygame.display.flip()
    clock.tick(60)