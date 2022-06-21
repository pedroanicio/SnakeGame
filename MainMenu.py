import pygame, sys
from button import Button

pygame.init()

Screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", 20)


def play():
    while True:
        import SnakeGame
        from SnakeGame import main
        main()


def main_menu():
    while True:
        Screen.blit(BG, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        menuText = get_font(100).render("Snake Game", True, "#b68f40")
        menuRect = menuText.get_rect(center=(250, 80))

        playButton = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(250, 200),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(250, 350),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        Screen.blit(menuText, menuRect)

        for button in [playButton, quitButton]:
            button.changeColor(menuMousePos)
            button.update(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    play()

                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()