import math

class Pakuri:
    def __init__(self, species, level):
        self.__species = species
        self.__level = level
        self.__attack = (len(species)*7 + 11)%16
        self.__defense = (len(species)*5 + 17)%16
        self.__stamina = (len(species)*6 + 13)%16
    def get_species(self):
        return self.__species
    def get_attack(self):
        return self.__attack
    def set_attack(self, new_attack):
        self.__attack = new_attack
    def get_defense(self):
        return self.__defense
    def get_stamina(self):
        return self.__stamina

    @property
    def cp(self):
        return math.floor(self.get_attack() * math.sqrt(self.get_defense()) * math.sqrt(self.get_stamina()) * self.level * .08)
    @property
    def hp(self):
        return math.floor(self.get_stamina()*self.level/6)
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, new_level):
        self.__level = new_level