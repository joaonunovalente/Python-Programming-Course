from datetime import datetime
import math, pygame

def get_time() -> tuple:
    hour: str = datetime.now().hour
    minute: str = datetime.now().minute
    second: str = datetime.now().second                 
    return (hour, minute, second)

def get_coordinates(angle, radius) -> tuple:
    x = window.get_width() / 2 + math.cos(math.radians(angle)) * radius 
    y = window.get_height() / 2 + math.sin(math.radians(angle)) * radius
    
    return (x, y)

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
            
    # Set time in the caption
    hour, minute, second = get_time()
    pygame.display.set_caption(f"{hour:02}:{minute:02}:{second:02}")

    # Get coordinates
    angle_seconds = (second * 6) - 90
    angle_minutes = (minute * 6) - 90
    angle_hours = (hour % 12 + minute / 60) * 30 - 90
    
    x_seconds, y_seconds = get_coordinates(angle_seconds, 100)
    x_minutes, y_minutes = get_coordinates(angle_minutes, 90)
    x_hours, y_hours = get_coordinates(angle_hours, 70)

    # Show time clock arrows
    window.fill((200, 200, 200))
    pygame.draw.circle(window, (0, 0, 0), (window.get_width() / 2, window.get_height() / 2), 150, 3)
    pygame.draw.line(window, (50, 50, 200), (window.get_width() / 2, window.get_height() / 2), (x_seconds, y_seconds), 1)
    pygame.draw.line(window, (50, 50, 200), (window.get_width() / 2, window.get_height() / 2), (x_minutes, y_minutes), 3)
    pygame.draw.line(window, (50, 50, 200), (window.get_width() / 2, window.get_height() / 2), (x_hours, y_hours), 5)

    # Add clock elements
    for i in range(12):
        x1 = 320 + math.cos(angle + i * math.pi / 6) * 140 
        y1 = 240 + math.sin(angle + i * math.pi / 6) * 140
        x2 = 320 + math.cos(angle + i * math.pi / 6) * 120 
        y2 = 240 + math.sin(angle + i * math.pi / 6) * 120
        pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 4)
    for i in range(4):
        x1 = 320 + math.cos(angle + i * math.pi / 2) * 140 
        y1 = 240 + math.sin(angle + i * math.pi / 2) * 140
        x2 = 320 + math.cos(angle + i * math.pi / 2) * 110 
        y2 = 240 + math.sin(angle + i * math.pi / 2) * 110
        pygame.draw.line(window, (0, 0, 0), (x1, y1), (x2, y2), 4)
    pygame.display.flip()

    clock.tick(60)