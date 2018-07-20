import random


class spell:
    def __init__(self,name,cost,dmg,type):
        self.name=name
        self.cost=cost
        self.dmg=dmg
        self.type=type

    def gen_magic_dmg(self):
        high=self.dmg+15
        low=self.dmg-15
        return random.randrange(low,high)


