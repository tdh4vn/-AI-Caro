import game_config as GameConfig
import pygame

pygame.init()
size = (GameConfig.window_width, GameConfig.window_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Caro - Nhap Mon Tri Tue Nhan Tao")

WHITE = (0xFF, 0xFF, 0xFF)
clock = pygame.time.Clock()
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
