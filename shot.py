import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, SHOT_RADIUS)