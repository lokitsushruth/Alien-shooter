import pygame
import sys

class Button:
    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _draw_explanation_screen(self):
        explanation_surface = pygame.Surface(self.screen.get_size())
        explanation_surface.set_alpha(200)  
        explanation_surface.fill((0, 0, 0))  
        self.screen.blit(explanation_surface, (0, 0))
        control_messages = [
            "Controls:",
            "Up - Move Up",
            "Down - Move Down",
            "Right - Move Right",
            "Left - Move Left",
            "Space - Shoot",
            "Q - Quit",
            "Made with love by Lokit "
        ]

        text_color = (255, 255, 255)
        font = pygame.font.SysFont(None, 30)
        line_height = 30
        x_position = self.screen_rect.centerx
        y_position = self.screen_rect.centery +50
        
        for message in control_messages:
            message_image = font.render(message, True, text_color)
            message_rect = message_image.get_rect(center=(x_position, y_position))
            self.screen.blit(message_image, message_rect)
            y_position += line_height

    def draw_button(self):
        self._draw_explanation_screen()  
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Button with Explanation")

