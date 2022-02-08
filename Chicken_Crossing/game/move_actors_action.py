
from game import constants
from game.action import Action
from game.point import Point
from game.handle_food_collisions import Handle_Food_Collision
from game.audio_service import AudioService

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        chicken = cast["chicken"][0]
        vel = chicken.get_velocity()
        vel = vel.get_x()
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

        if vel < 0:
            chicken.set_image(constants.IMAGE_CHICKEN_LEFT)
   
        elif vel > 0:
            chicken.set_image(constants.IMAGE_CHICKEN)

        pos = chicken.get_position()
        pos = pos.get_x()
        if pos > 180 and pos < 185:
            if vel > 0:
                audio_service.play_sound(constants.CAR_HONK)
        if pos > 480 and pos < 485 :
            if vel < 0:
                audio_service.play_sound(constants.CAR_HONK)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(position)        