"""
Pong (Single Player)
====================

A pong game. (reference implementation)
"""
import pygame


class Pong:
    """
    Pong(self)

    The object for pong game.
    """
    HEIGHT = 800
    WIDTH = 1600

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 10
    BALL_VELOCITY = 10

    COLOR = (255, 255, 255)

    def __init__(self):
        """
        Initialize self.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 800))
        self.clock = pygame.time.Clock()

    def game_loop(self):
        """
        Game loop for pong.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE:
                    return


class Paddle(pygame.Rect):
    """
    Paddle(self, velocity, up_key, down_key, *args, **kwars)

    A paddle object.

    Parameters
    ----------

    velocity : int
        The velocity of paddle.
    up_key : pygame.key
        The key to trigger up movement of paddle.
    down_key : pygame.key
        The key to trigger down movement of paddle
    """
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        """
        Initialize self.
        """
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)


class Ball(pygame.Rect):
    """
    Ball(self, velocity, *args, **kwargs)

    A ball object.

    Parameters
    ----------

    velocity : int
        The velocity of the ball.
    """
    def __init__(self, velocity, *args, **kwargs):
        """
        Initialize self.
        """
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)
