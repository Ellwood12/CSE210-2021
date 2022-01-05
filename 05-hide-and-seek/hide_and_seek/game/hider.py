import random

class Hider:
    """A code template for our hider. The responsibility of this class of
    objects is to watch the seeker and give hints.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the hider (1-1000).
        distance (list): The distance from the seeker.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self):
        """Gets a hint for the hunter.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        hint = "(-.-) Maybe I'll take a nap."
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint
        
    def watch(self, location):
        """Watches the given location by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)