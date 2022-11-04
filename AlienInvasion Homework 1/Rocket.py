import sys
import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #Load the ship image and get its rect.
        self.image = pygame.image.load('../images/ship.bmp').convert_alpha()
        #self.image.set_colorkey((230,230,230))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center
        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update moving the ships position based on the movement flag"""
        #updates the ships x/y value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1.5
        if self.moving_left and self.rect.left > 0:
            self.x -= 1.5
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5
        #update the rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Inatilize the game , and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        #respond to key presses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self,event):
        #respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.bg_color)
        # redraw the screen during each pass through the loop
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game( )