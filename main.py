import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    game_clock = pygame.time.Clock()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                sys.exit(f"Game over! You ended with a score of {score}.")
            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    score += 1
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        text = font.render(f"Score: {score}", False, "White")
        screen.blit(text, (0,0))
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()