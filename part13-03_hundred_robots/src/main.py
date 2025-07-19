from random import randint
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))


robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

for i in range(0,1000):
    x = randint(0, 590)
    y = randint(0, 390)
    window.blit(robot, (x, y))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()