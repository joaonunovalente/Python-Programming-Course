import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))


robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

height = 100
for i in range(0, 10):
    width = 50 + i * 50
    window.blit(robot, (width, height))
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()