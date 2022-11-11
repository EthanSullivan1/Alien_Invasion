import sys
import pygame
from settings import Settings
from Raindrop import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Inatilize the game , and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.aliens = pygame.sprite.Group()
        self.create_fleet()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_aliens()
            self._update_screen()
    def _update_aliens(self):
        self.aliens.update()

        make_new_aliens = False
        for drop in self.aliens.copy():
            if drop.check_disappeared():

                self.aliens.remove(drop)
                make_new_aliens = True

        if make_new_aliens:
            self._create_row(0)


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self,event):
        #respond to key presses
        if event.key == pygame.K_q:
            sys.exit()



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        # redraw the screen during each pass through the loop
        self.aliens.draw(self.screen)
        #Make the most recently drawn screen visible.
        pygame.display.flip()
    def create_fleet(self):
        """Creates the aline fleet"""
        #make and alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (alien_width)

        self.number_aliens_x = available_space_x//(2 * alien_width)

        #determine the number of rows of aliens that fit on the screen
        available_space_y = (self.settings.screen_height)
        number_rows = available_space_y // (2*alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        for alien_number in range(self.number_aliens_x):
            self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien.rect.height* row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game( )