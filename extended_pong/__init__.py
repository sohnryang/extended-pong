"""__init__.py"""


def main():
    """main function"""
    from extended_pong.pong import Pong
    game = Pong()
    game.game_loop()
