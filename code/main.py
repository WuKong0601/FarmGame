import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Life of a chill Guy')
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Start menu
        self.show_intro = True


        self.intro_background = pygame.image.load('../graphics/start_menu/start_menu.png').convert_alpha()
        self.start_button = pygame.image.load('../graphics/start_menu/start_button.png').convert_alpha()


        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))


        button_width = int(SCREEN_WIDTH * 0.2)
        button_height = int(button_width * 0.5)
        self.start_button = pygame.transform.scale(self.start_button, (button_width, button_height))


        self.start_button_rect = self.start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN and self.show_intro:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.show_intro = False

            dt = self.clock.tick() / 1000


            if self.show_intro:
                self.screen.blit(self.intro_background, (0, 0))
                self.screen.blit(self.start_button, self.start_button_rect)
            else:
                self.level.run(dt)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    try:
        game.run()
    finally:
        # Lưu dữ liệu người chơi khi thoát trò chơi
        game.level.player.save_data()