import pygame

class RobotGame:
    def __init__(self):
        pygame.init()
        self.window_height = 1080
        self.window_width = 1920
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Robot Game")
        self.load_images()
        self.robot = Robot(
            self.window_width // 2,
            self.window_height - self.images["robot"].get_height(),
            self.images["robot"],
            self.window
        )
        self.coins = []
        self.monsters = []
        self.doors = []
        self.spawn_coins = CoinSpawn()
        self.spawn_monsters = MonsterSpawn()
        self.spawn_doors = DoorSpawn()
        self.score = 0
        self.health = 3
        self.total_coins = 100
        self.total_health = 3
        self.font = pygame.font.SysFont('Arial', 30)
        self.main_loop()

    def load_images(self):
        self.images = {}
        for name in ["door", "coin", "robot", "monster"]:
            try:
                self.images[name] = pygame.image.load(f"{name}.png")
            except FileNotFoundError:
                print(f"Error: Could not load image {name}.png")
                pygame.quit()
                exit()

    def main_loop(self):
        while True:
            self.check_events()
            self.generate()
            self.update()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.robot.set_movement("left", True)
                if event.key == pygame.K_RIGHT:
                    self.robot.set_movement("right", True)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.robot.set_movement("left", False)
                if event.key == pygame.K_RIGHT:
                    self.robot.set_movement("right", False)
            elif event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.FINGERDOWN:
                    x, y = event.x * self.window_width, event.y * self.window_height
                else:
                    x, y = pygame.mouse.get_pos()
                column_width = self.window_width // 3
                if x < column_width:
                    self.robot.set_movement("left", True)
                elif x > 2 * column_width:
                    self.robot.set_movement("right", True)
            elif event.type == pygame.FINGERUP or event.type == pygame.MOUSEBUTTONUP:
                self.robot.set_movement("left", False)
                self.robot.set_movement("right", False)

    def generate(self):
        # Generate coins
        coin = self.spawn_coins.generate(
            self.window,
            self.images["coin"],
            robot=self.robot
        )
        if coin:
            self.coins.append(coin)
        # Generate monsters
        monster = self.spawn_monsters.generate(
            self.window,
            self.images["monster"],
            robot=self.robot
        )
        if monster:
            self.monsters.append(monster)
        # Generate doors
        door = self.spawn_doors.generate(
            self.window,
            self.images["door"],
            robot=self.robot
        )
        if door:
            self.doors.append(door)

    def update(self):
        self.spawn_coins.update()
        self.spawn_monsters.update()
        self.spawn_doors.update()
        self.robot.update()

        self.coins = [coin for coin in self.coins if coin.y < self.window_height]
        for coin in self.coins[:]:
            coin.update()
            if self.robot.get_rect().colliderect(coin.get_rect()):
                self.coins.remove(coin)
                self.score += 1
                print(f"Coin collected! Score: {self.score}")
                if self.score >= self.total_coins:
                    self.show_popup("You Win!")
            elif coin.y >= self.window_height:
                self.coins.remove(coin)
                self.health -= 1
                print(f"Coin missed! Health: {self.health}")
                if self.health <= 0:
                    self.show_popup("Game Over!")

        self.monsters = [monster for monster in self.monsters if monster.y < self.window_height]
        for monster in self.monsters[:]:
            monster.update()
            if self.robot.get_rect().colliderect(monster.get_rect()):
                self.monsters.remove(monster)
                self.health -= 1
                print(f"Monster hit! Health: {self.health}")
                if self.health <= 0:
                    self.show_popup("Game Over!")
            elif monster.y > self.window_height:
                self.monsters.remove(monster)

        self.doors = [door for door in self.doors if door.y < self.window_height]
        for door in self.doors[:]:
            door.update()
            if self.robot.get_rect().colliderect(door.get_rect()):
                self.doors.remove(door)
                self.health = min(self.total_health, self.health + 1)
                print(f"Health restored! Health: {self.health}")
            elif door.y > self.window_height:
                self.doors.remove(door)

    def draw_window(self):
        self.window.fill((230, 230, 230))
        self.draw_objects()
        coin_text = self.font.render(f"{self.score} / {self.total_coins}", True, (0, 0, 0))
        self.window.blit(self.images['coin'], (self.window.get_width() - 180, 19))
        self.window.blit(coin_text, (self.window_width - coin_text.get_width() - 20, 20))
        door_text = self.font.render(f"{self.health} / {self.total_health}", True, (0, 0, 0))
        self.window.blit(self.images['door'], (self.window.get_width() - 184, 65))
        self.window.blit(door_text, (self.window_width - door_text.get_width() - 37, 83))
        pygame.display.flip()

    def draw_objects(self):
        self.robot.draw(self.window)
        for coin in self.coins:
            coin.draw(self.window)
        for monster in self.monsters:
            monster.draw()
        for door in self.doors:
            door.draw()

    def show_popup(self, message):
        popup_font = pygame.font.SysFont('Arial', 50)
        button_font = pygame.font.SysFont('Arial', 30)

        popup_surface = pygame.Surface((600, 300))
        popup_surface.fill((200, 200, 200))
        popup_rect = popup_surface.get_rect(center=(self.window_width // 2, self.window_height // 2))

        text = popup_font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(300, 100))
        popup_surface.blit(text, text_rect)

        pygame.draw.rect(popup_surface, (100, 100, 100), (200, 180, 200, 60))
        button_text = button_font.render("Quit", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(300, 210))
        popup_surface.blit(button_text, button_rect)

        self.window.blit(popup_surface, popup_rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if popup_rect.collidepoint(mouse_pos):
                        x, y = mouse_pos[0] - popup_rect.left, mouse_pos[1] - popup_rect.top
                        if 200 <= x <= 400 and 180 <= y <= 240:
                            waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        waiting = False

        pygame.quit()
        exit()
        
class Robot:
    def __init__(self, x, y, image, window):
        self.x = x
        self.y = y
        self.image = image
        self.to_left = False
        self.to_right = False
        self.window = window

    def set_movement(self, direction, is_pressed):
        if direction == "left":
            self.to_left = is_pressed
        if direction == "right":
            self.to_right = is_pressed

    def update(self):
        if self.to_left and self.x > 0:
            self.x -= 1.5
        if self.to_right and self.x < self.window.get_width() - self.image.get_width():
            self.x += 1.5

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


    @property
    def get_position(self):
        return self.x, self.y
    
class Coin:
    def __init__(self, x, y, image, window):
        self.x = x
        self.y = y
        self.image = image
        self.velocity = 0.3
        self.window = window

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.velocity

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

class Monster:
    def __init__(self, x, y, image, window):
        self.x = x
        self.y = y
        self.image = image
        self.window = window
        self.speed = 0.35

    def update(self):
        self.y += self.speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
    
class Door:
    def __init__(self, x, y, image, window):
        self.x = x
        self.y = y
        self.image = image
        self.window = window
        self.speed = 0.4

    def update(self):
        self.y += self.speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

class Spawn:
    def __init__(self, spawn_interval=500, min_spawn_interval=300):
        self.spawn_counter = 0
        self.spawn_interval = spawn_interval
        self.min_spawn_interval = min_spawn_interval
        self.spawn_position = 0

    def update(self):
        self.spawn_counter += 1

class CoinSpawn(Spawn):
    def __init__(self):
        super().__init__(spawn_interval=1200, min_spawn_interval=600)
        self.spawn_position = 0

    def generate(self, window, image, robot, **kwargs):
        if self.spawn_counter >= self.spawn_interval:
            self.spawn_interval = max(
                self.min_spawn_interval,
                self.spawn_interval - 5
            )
            self.spawn_counter = 0

            self.spawn_position = (self.spawn_position * 3 + robot.x + 150) % (window.get_width() - image.get_width())

            return self._create_object(
                self.spawn_position,
                0,
                image,
                window,
                **kwargs
            )
        return None

    def _create_object(self, x, y, image, window):
        return Coin(x, y, image, window)

class MonsterSpawn(Spawn):
    def __init__(self):
        super().__init__(spawn_interval=1600, min_spawn_interval=800)
        self.spawn_position = 300

    def generate(self, window, image, robot, **kwargs):
        if self.spawn_counter >= self.spawn_interval:
            self.spawn_interval = max(
                self.min_spawn_interval,
                self.spawn_interval - 100
            )
            self.spawn_counter = 0

            self.spawn_position = (self.spawn_position * 2 + robot.x + 200) % (window.get_width() - image.get_width())

            return self._create_object(
                self.spawn_position,
                0,
                image,
                window,
                **kwargs
            )
        return None

    def _create_object(self, x, y, image, window):
        return Monster(x, y, image, window)

class DoorSpawn(Spawn):
    def __init__(self):
        super().__init__(spawn_interval=20000, min_spawn_interval=15000)
        self.spawn_position = 0

    def generate(self, window, image, robot, **kwargs):
        if self.spawn_counter >= self.spawn_interval:
            self.spawn_interval = max(
                self.min_spawn_interval,
                self.spawn_interval - 200
            )
            self.spawn_counter = 0

            self.spawn_position = (self.spawn_position * 2 + robot.x + 250) % (window.get_width() - image.get_width())

            return self._create_object(
                self.spawn_position,
                0,
                image,
                window,
                **kwargs
            )
        return None

    def _create_object(self, x, y, image, window):
        return Door(x, y, image, window)


if __name__ == "__main__":
    RobotGame()
