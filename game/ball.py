import pygame
import random
import os

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

        # Initialize mixer
        pygame.mixer.init()

        # Sounds folder path
        current_dir = os.path.dirname(os.path.abspath(__file__))  # points to game/
        sounds_path = os.path.join(current_dir, "sounds")  # game/sounds

        self.sounds = {
            "paddle": pygame.mixer.Sound(os.path.join(sounds_path, "paddle_hit.wav")),
            "wall": pygame.mixer.Sound(os.path.join(sounds_path, "wall_bounce.wav")),
            "score": pygame.mixer.Sound(os.path.join(sounds_path, "score.wav"))
        }

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall collision
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            self.sounds["wall"].play()

    def check_collision(self, player, ai):
        if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
            self.velocity_x *= -1
            self.sounds["paddle"].play()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        self.sounds["score"].play()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
