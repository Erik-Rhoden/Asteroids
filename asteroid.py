import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            vector = self.velocity.rotate(angle)
            neg_vector = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            
            pos_asteroid.velocity = vector * 1.2
            neg_asteroid.velocity = neg_vector * 1.2