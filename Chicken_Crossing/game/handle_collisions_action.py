import random
from game.action import Action
from game.physics_service import PhysicsService
from game.point import Point
from game.actor import Actor
from game.audio_service import AudioService
from game import constants

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self) -> None:
        super().__init__()
        self._keep_playing= True
    
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        chicken = cast["chicken"][0] # there's only one
        cars = cast["cars"] # there's only one
        trucks = cast["trucks"]
        semi_trucks = cast["semi_trucks"]
        eagles = cast["eagle"]

        value = PhysicsService()
        for car in cars:
            experiment = value.is_collision(chicken, car)
            if experiment == True:
                #print("Chicken Touching Car")
                audio_service.play_sound(constants.HIT_CHICKEN)
                self._keep_playing = False

        value2 = PhysicsService()
        for truck in trucks:
            experiment2 = value2.is_collision(chicken, truck)
            if experiment2 == True:
                #print("Chicken Touching Truck")
                audio_service.play_sound(constants.HIT_CHICKEN)
                self._keep_playing = False
  
        value3 = PhysicsService()
        for semi_truck in semi_trucks:
            experiment3 = value3.is_collision(chicken, semi_truck)
            if experiment3 == True:
                #print("Chicken Touching Semi_Truck")
                audio_service.play_sound(constants.HIT_CHICKEN)
                self._keep_playing = False
 
        value4 = PhysicsService()
        for eagle in eagles: 
            experiment4 = value4.is_collision(chicken, eagle)
            if experiment4 == True:
                #print("Chicken Touching Eagle")
                audio_service.play_sound(constants.EAGLE)
                self._keep_playing = False

        
    
