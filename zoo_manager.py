class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"Animal sound"

class Aviary:
    def __init__(self):
        self.birds = []
    
    def store_birds(self, new_bird):
        self.birds.append(new_bird)
    
    def display_birds(self):
        for bird in self.birds:
            print(f"{bird.name} - {bird.species} - {bird.wingspan}")

class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []
    
    def store_reptiles(self, new_reptile):
        self.reptiles.append(new_reptile)
    
    def display_reptiles(self):
        for reptile in self.reptiles:
            print(f"{reptile.name} - {reptile.species}")