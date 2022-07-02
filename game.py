import pygame
from ball import Ball
from danger import Danger


class Game():

    def __init__(self) -> None:
        '''Constructor to initalize an object of class game
        Paramters:
        -> None
        '''
        # Initialize pygame modules
        pygame.init()

        # Definition of all game colours
        self.white = (255, 255, 255)
        self.blue = (50, 153, 213)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 102)
        self.start_menu = True
        self.game_over = False
        self.game_close = False
        self.counter_miss = 0
        self.counter_caught = 0
        self.danger = 0
        self.width = 50
        self.height = 15
        self.objects = []
        self.total_time_elapsed = 0
        self.time_elapsed_since_last_action = 0
        self.time_elapsed_since_last_action_danger = 0

        # Definition of game font
        self.score_font = pygame.font.SysFont("comicsansms", 35)

        # Setting dimensions of the display
        self.dis_width = 800
        self.dis_height = 600
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))

        # Setting a caption for the display
        pygame.display.set_caption('Game')

    def reset_game(self):
        self.total_time_elapsed = 0
        self.time_elapsed_since_last_action = 0
        self.time_elapsed_since_last_action_danger = 0
        self.objects.clear()
        self.counter_miss = 0
        self.counter_caught = 0
        self.danger = 0
        self.game_close = False
        self.game_over = False

    def message(self, msg, color, position, font_size) -> None:
        '''Function to print a message to the display
        Paramters:
        msg (str): The message to be printed
        position (list): The position of the message to be printed on the screen
        '''
        mesg = font_size.render(msg, True, color)
        self.dis.blit(mesg, position)

    def display_score(self, score, missed, danger) -> None:
        score = "Your Score: " + str(score)
        missed = "You missed: " + str(missed)
        danger = "Dangerous objects: " + str(danger)

        self.message(score, self.red, [0, 0], pygame.font.SysFont(None, 50))
        self.message(missed, self.red, [0, 50], pygame.font.SysFont(None, 50))
        self.message(danger, self.red, [0, 100], pygame.font.SysFont(None, 50))
