import random

class dice:
    def __init__(self, s):
        self.sides_count = 6
        random.seed(s)
    def roll(self):
        return random.randrange(1, self.sides_count + 1)






