import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    Tron motorcycle look a like 
    
    The responsibility of cycle is to move itself.

    Attributes:
        _segments[] = : holds a collection of the initial segments of a cycle 
                        and receives the additional segments as the cycle grows.
    """
    def __init__(self, color):
        super().__init__()
        self.set_color(color)
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """Gets the Cycle's segments as a [].
        
        Returns:
            _segments: The Cycles's body segments as it grows.
        """
        return self._segments

    def move_next(self):
        """Moves the cycles's color towards the velocity point 
            and uses the grow_tail() and the move_next() from Actor claas
            to increase size as it moves.
        
        Args:
            grow_tail(1, self.get_color): the tail grows with the initial color of the cycle.
            move_next(): moves each segmet to a new direction
        """

        # move all segments
        self.grow_tail(1, self.get_color())
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets the first segmen of the cycle.
        
        Returns:
            segment: The actor's position, velocity, text and color.
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):

        """Grows the actor's tail.
        
        Returns:
            segment: new segment appended to the cycle's body.
        """
        
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """turns the actor's first segment.
        
        Args:
            set_velocity(velocity)
        Returns:
            _segments[0]: The actor's first segment with a new velocity.
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Creates the initial body of the cycles with their own color.
        
            Args:
            Point class
            and several methods from the Actor class.  
        """
        x = 0.0
        y = 0.0
        if (self.get_color() == constants.RED):
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 4)
        else:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            #color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self.get_color())
            self._segments.append(segment)