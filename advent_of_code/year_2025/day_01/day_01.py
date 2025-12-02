from typing  import assert_never

class Safe:
    """ This is an object that represents the safe """
    def __init__(self, initial_position: int = 50):
        self._position = initial_position

        # initialize the combination to zero
        self._combination = 0

        self._click_combination = 0
    
    def move(self, move_spec: str) -> None:
        # parse move into direction and amount
        dir, amount = move_spec[0], int(move_spec[1:])

        
        if dir.upper() == 'L':
            amount = - amount
        elif dir.upper() == 'R':
            pass
        else:
            assert_never

        # move the dial
        old_position = self._position

        self._position = (self._position + amount) % 100

        # if the count is zero, that is part of the combination for the non-click safe
        if self.current_position == 0:
            self._combination += 1

        # update the click combination by counting the number of clicks
        if amount > 0:
            # right move
            self._click_combination += (old_position + amount) // 100
        else:
            # left move. This is more complicated because the I need the dial position as a negative number
            self._click_combination += ((old_position % -100) + amount) // -100

    @property
    def current_position(self) -> int:
        return self._position
    
    @property
    def combination(self) -> int:
        return self._combination

    @property
    def click_combination(self) -> int:
        return self._click_combination
    