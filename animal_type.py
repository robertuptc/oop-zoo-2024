from zoo_manager import Animal, Aviary, ReptileEnclosure

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan


class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"
    

class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"


class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"


bird = Bird("Eagle", "Aquila chrysaetos", wingspan=2.5)
bird2 = Bird("woodpecker", "not sure", wingspan=2)

aviary = Aviary()
# print(aviary.birds)
aviary.store_birds(bird)
aviary.store_birds(bird2)
# print(aviary)
aviary.display_birds()


reptile = Reptile('turtle', 'Green Sea Turtle')
reptiles = ReptileEnclosure()
reptiles.store_reptiles(reptile)
reptiles.display_reptiles()
