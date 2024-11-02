import pygame
import os

pygame.init()
#global variables
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino","DinoRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("Assets/Dino","DinoJump.png")),]
DUCKING = [pygame.image.load(os.path.join("Assets/Dino","DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino","DinoDuck2.png"))]


SMALL_Cactus = [pygame.image.load(os.path.join("Assets/Cactus","SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus","SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus","SmallCactus3.png"))]
LARGE_Cactus = [pygame.image.load(os.path.join("Assets/Cactus","LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus","LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus","LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird","Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird","Bird2.png"))]