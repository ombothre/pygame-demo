import random
from pygame import image, mixer, Surface

class Player:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.img = image.load('assets/images/player.png')
        self.x = 370
        self.y = 480
        self.x_change = 0

    def move(self, direction: str):
        self.x_change = -5 if direction == 'left' else 5

    def stop_move(self):
        self.x_change = 0

    def update(self):
        self.x += self.x_change
        self.x = max(0, min(self.x, 736))

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

class Bullet:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.img = image.load('assets/images/bullet.png')
        self.x = 0
        self.y = 480
        self.y_change = 10
        self.state = "ready"
        self.sound = mixer.Sound("assets/audio/laser.wav")

    def fire(self, player_x: int):
        if self.state == "ready":
            self.state = "fire"
            self.x = player_x
            self.sound.play()

    def update(self):
        if self.state == "fire":
            self.y -= self.y_change
            if self.y <= 0:
                self.reset()

    def reset(self):
        self.y = 480
        self.state = "ready"

    def draw(self):
        if self.state == "fire":
            self.screen.blit(self.img, (self.x + 6, self.y + 4))

class Enemy:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.img = image.load('assets/images/enemy.png')
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.x_change = 4
        self.y_change = 40

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= 736:
            self.x_change *= -1
            self.y += self.y_change

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))