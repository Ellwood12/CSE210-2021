from game.actor import Actor
from game import constants
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
import time
import raylibpy



class End_Game(Action):
    def __init__(self) -> None:
        super().__init__()
        self._end = False

    def execute(self, cast):
        end = Actor()
        audio_service = AudioService()
        end_info = []
        bricks = len(cast["bricks"])
        ball = cast["balls"][0]
        y_pos = ball._position.get_y()
  
        if bricks == 0:
            #audio_service.play_sound(constants.SOUND_OVER)
            end.set_image(constants.IMAGE_END)
            end.set_height(50)
            end.set_width(50)
            end_pos = Point(120,80)
            end.set_position(end_pos)
            end_info.append(end)
            cast["end"] = end_info

        if y_pos >= 580:
            end.set_image(constants.IMAGE_END)
            end.set_height(50)
            end.set_width(50)
            end_pos = Point(120,80)
            end.set_position(end_pos)
            end_info.append(end)
            cast["end"] = end_info
            new_vel = Point(0, 0)
            ball.set_velocity(new_vel)

        cast["end"] = end_info


