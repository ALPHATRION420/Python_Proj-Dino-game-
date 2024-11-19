#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[3]:


pip install panadas


# In[4]:


pip install pygame


# In[5]:


pip install matplotlib


# In[6]:


pip install time


# In[7]:


pip install default


# In[8]:


pip install random


# In[21]:


import pygame
import random
import time

# Initialize Pygame
pygame.init()

dino_path = r"C:\Users\saxen\OneDrive\Desktop\dino.png"
cactus_path = r"C:\Users\saxen\OneDrive\Desktop\cactus.png"

# Constants
WIDTH, HEIGHT = 800, 400
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = 15
CACTUS_SPEED = 8
CACTUS_SPAWN_INTERVAL = 1200  # in milliseconds (1.2 seconds)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (135, 206, 235)  # Sky blue for the background

# Sprite Grouping
all_sprites = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()

# Dino Class (Sprite-based)
class Dino(pygame.sprite.Sprite):
    def __init__(self):  # Corrected __init__ method
        super().__init__()
        # Load the dino sprite from the specified desktop path
        self.image = pygame.image.load(dino_path)
        self.image = pygame.transform.scale(self.image, (80, 80))  # Resize to smaller size (80x80)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT - self.rect.height  # Position at the bottom of the screen
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = -JUMP_STRENGTH
            self.is_jumping = True

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.y >= HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
            self.is_jumping = False
            self.velocity_y = 0

# Cactus Class (Sprite-based)
class Cactus(pygame.sprite.Sprite):
    def __init__(self):  # Corrected __init__ method
        super().__init__()
        # Load cactus sprite and resize it to a smaller size (40x60)
        self.image = pygame.image.load(cactus_path)  # Make sure to replace with your cactus image
        self.image = pygame.transform.scale(self.image, (40, 60))  # Resize the cactus sprite
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - self.rect.height  # Position at the bottom of the screen

    def update(self):
        self.rect.x -= CACTUS_SPEED
        if self.rect.x < -self.rect.width:  # If cactus moves off screen
            self.rect.x = WIDTH + random.randint(50, 200)  # Reset position to the right

    def reset(self):
        self.rect.x = WIDTH + random.randint(50, 200)  # Reset cactus position

# Main Game Class
class DinoGame:
    def __init__(self):  # Corrected __init__ method
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dino Game")
        self.clock = pygame.time.Clock()
        self.dino = Dino()
        all_sprites.add(self.dino)
        self.cactuses = []
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 32)
        self.running = True  # Initialize 'running' attribute
        self.last_cactus_time = pygame.time.get_ticks()
        self.game_over = False

    def spawn_cactus(self):
        if pygame.time.get_ticks() - self.last_cactus_time > CACTUS_SPAWN_INTERVAL:
            cactus = Cactus()
            self.cactuses.append(cactus)
            cactus_group.add(cactus)
            all_sprites.add(cactus)
            self.last_cactus_time = pygame.time.get_ticks()

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))

    def display_game_over(self):
        game_over_text = self.font.render("Game Over", True, BLACK)
        score_text = self.font.render(f"Final Score: {self.score}", True, BLACK)
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))

    def run(self):
        while self.running:
            self.screen.fill(BACKGROUND_COLOR)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Key handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.dino.is_jumping:
                self.dino.jump()

            # Update game state
            all_sprites.update()
            self.spawn_cactus()

            # Check for collisions between Dino and Cactus
            if pygame.sprite.spritecollide(self.dino, cactus_group, False):
                self.game_over = True
                self.running = False

            # Update score
            if not self.game_over:
                self.score += 1

            # Draw everything
            all_sprites.draw(self.screen)
            self.display_score()

            # Game over screen
            if self.game_over:
                self.display_game_over()

            pygame.display.flip()

            # Frame rate control
            self.clock.tick(FPS)

        # Wait for a few seconds before closing the game
        if self.game_over:
            time.sleep(2)

        pygame.quit()

# Start the game
game = DinoGame()
game.run()


# In[ ]:





# In[ ]:





# In[ ]:




