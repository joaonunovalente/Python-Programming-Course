from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and robot_x < event.pos[0] < robot_x + robot.get_width() and robot_y < event.pos[1] < robot_y + robot.get_height():
            target_x = randint(0, 640 - robot.get_width())
            target_y = randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit(0)
    robot_x = target_x
    robot_y = target_y

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)