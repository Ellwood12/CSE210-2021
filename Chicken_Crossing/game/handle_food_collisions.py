from game.action import Action
from game.physics_service import PhysicsService
import random
from game.point import Point
from game.score import Score
from game.actor import Actor
from game.seed import Seed
from game.chicken import Chicken
from game import constants
from game.audio_service import AudioService


class Handle_Food_Collision(Action):
    def __init__(self) -> None:
        
        """Handles collisions between the snake's head and the food. Grows the 
        snake, updates the score and moves the food if there is one.

        Args:
            self (Director): An instance of Director.
        """
        self._points = 0
    def execute(self, cast):
        audio_service = AudioService()
        chicken = cast["chicken"][0]
        seed = cast["seeds"][0]

        value = PhysicsService()
        score = Score()
        experiment = value.is_collision(chicken, seed)
        if experiment == True:
            if seed._position.get_x() == 750:
                new_position_left = Point(50,random.randint(50,500))
                seed.set_position(new_position_left)
                self._points += 1

                score = Score()
                score_info = []
                position = Point(1, 0)
                score.set_height(20)
                score.set_width(20)
                position = Point(1, 0)
                score.set_position(position)
                score.set_text(f"Score: {self._points}")
                score_info.append(score)
                cast["score"] = score_info              

            elif seed._position.get_x() == 50:
                new_position_right = Point(750,random.randint(50,500))
                seed.set_position(new_position_right)
                self._points += 1

                score = Score()
                score_info = []
                position = Point(1, 0)
                points = 0
                score.set_height(20)
                score.set_width(20)
                position = Point(1, 0)
                score.set_position(position)
                score.set_text(f"Score: {self._points}")
                score_info.append(score)
                cast["score"] = score_info

        if self._points >= 4:
            #chicken.set_image(constants.IMAGE_PIG)
            constants.IMAGE_CHICKEN = constants.IMAGE_PIG
            constants.IMAGE_CHICKEN_LEFT = constants.IMAGE_PIG_LEFT

        if self._points >= 8:
            #chicken.set_image(constants.IMAGE_PIG)
            constants.IMAGE_CHICKEN = constants.IMAGE_CHICKEN_BACK
            constants.IMAGE_CHICKEN_LEFT = constants.IMAGE_CHICKEN_LEFT_BACK

        if self._points >= 12:
            #chicken.set_image(constants.IMAGE_PIG)
            constants.IMAGE_CHICKEN = constants.IMAGE_PIG
            constants.IMAGE_CHICKEN_LEFT = constants.IMAGE_PIG_LEFT

        if self._points >= 16:
            #chicken.set_image(constants.IMAGE_PIG)
            constants.IMAGE_CHICKEN = constants.IMAGE_CHICKEN_BACK
            constants.IMAGE_CHICKEN_LEFT = constants.IMAGE_CHICKEN_LEFT_BACK
        


            
