import pygame
a=pygame.init()
pygame.display.set_mode((1200,600))
pygame.display.set_caption("NIKUNJ's FIRST GAME")
exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("HIIIIIII")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("Hlwww")

pygame.quit()
quit()