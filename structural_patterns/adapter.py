import math

class RoundHole:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()
    

class RoundPeg:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquarePeg:
    def __init__(self, width) -> None:
        self.width = width

    def get_witdh(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg) -> None:
        self.square_peg = square_peg
    
    def get_radius(self):
        return self.square_peg.get_witdh() * math.sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(5)
    round_peg = RoundPeg(5)
    hole.fits(round_peg)

    small_square_peg = SquarePeg(5)
    large_square_peg = SquarePeg(10)
    try:
        hole.fits(small_square_peg)
    except AttributeError as attr_error:
        print(attr_error)

    small_square_peg_adapter = SquarePegAdapter(small_square_peg)
    large_square_peg_adapter = SquarePegAdapter(large_square_peg)

    print(f'The small square peg fit? {hole.fits(small_square_peg_adapter)}')
    print(f'The large square peg fit? {hole.fits(large_square_peg_adapter)}')
