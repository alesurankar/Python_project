import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Pygame Window")
clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fill screen with black
        screen.fill((0, 0, 0))
    
        # Update the display
        pygame.display.flip()

        # 60 frames per second
        clock.tick(60)
    
# Quit pygame properly
pygame.quit()