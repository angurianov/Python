
class Hero():
    """Class to create Hero"""
    def __init__(self, name, level, race):
        """Initiate of hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this hero"""
        description = (self.name + " Level is:" + str(self.level) + " Race is:" + self.race + " Health is" + str(self.health)).title()
        print(description)


    def level_up(self):
        """Upgrade level of hero"""
        self.level = self.level + 1

    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + " start moving")


class SuperHero(Hero):
    """Class to create super hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use magic"""
        self.magic = self.magic - 10
        self.magic -= 10

    def show_hero(self):
        """Print all parameters of this hero"""
        description = (self.name + " Level is:" + str(self.level) + " Race is:" + self.race +
                       " Health is" + str(self.health) + " Magic is:" + str(self.magic)).title()
        print(description)
