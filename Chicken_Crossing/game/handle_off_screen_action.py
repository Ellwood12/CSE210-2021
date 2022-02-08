from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.actor import Actor
import random

class HandleOffScreenAction():
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        chicken = cast["chicken"][0]
        eagle = cast["eagle"][0]
        x_pos = chicken._position.get_x()
        if x_pos >= 780:
            new_pos = Point(780, chicken._position._y)
            chicken.set_position(new_pos)

        elif x_pos <= 18:
            new_pos = Point(18, chicken._position._y)
            chicken.set_position(new_pos)

        y_pos = chicken._position.get_y()
        if y_pos >= 580:
            new_pos = Point(chicken._position._x, 580)
            chicken.set_position(new_pos)

        elif y_pos <= 18:
            new_pos = Point(chicken._position._x, 18)
            chicken.set_position(new_pos)

        eagle_position = eagle._position.get_x()
        if eagle_position <=10:
            new_location =  Point(800, random.randint(1,550))
            eagle.set_position(new_location)
            new_velocity = Point(-(random.randint(2,6)),0)
            eagle.set_velocity(new_velocity)

    
