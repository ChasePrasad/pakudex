from pakuri import Pakuri as pak

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuris = []
    
    def get_size(self):
        return len(self.pakuris)
    
    def get_capacity(self):
        return self.capacity
    
    def get_species_array(self):
        return [pakuri.get_species() for pakuri in self.pakuris] if len(self.pakuris) > 0 else None
    
    def get_stats(self, species):
        for pakuri in self.pakuris:
            if species == pakuri.get_species():
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
            
        return None
    
    def sort_pakuri(self):
        self.pakuris.sort()

    def add_pakuri(self, species):
        for pakuri in self.pakuris:
            if species == pakuri.get_species():
                return False
        
        self.pakuris.append(pak(species))
        return True
    
    def evolve_species(self, species):
        for pakuri in self.pakuris:
            if species == pakuri.get_species():
                pakuri.evolve()
                return True
            
        return False