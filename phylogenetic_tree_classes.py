class Life:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


#Life Subclasses
class Bacteria(Life):
    def __str__(self):
        return 'Bacteria: "%s"' % self.name

class Archaea(Life):
    def __str__(self):
        return 'Archaea: %s"' % self.name

class Eucarya(Life):
    def __str__(self):
        return '"Eucarya: %s"' % self.name


#Bacteria Subclasses
class Thermotoga(Bacteria):
    pass

class Bacteroides(Bacteria):
    pass

class Cyanobacteria(Bacteria):
    pass

class PurpleBacteria(Bacteria):
    pass

class GramPositives(Bacteria):
    pass

class GreenNonsulfurBacteria(Bacteria):
    pass


#Archaea Subclasses
class ThermoproteusPryodicium(Archaea):
    pass

class Thermococcales(Archaea):
    pass

class Methancoccales(Archaea):
    pass

class Methanobactertales(Archaea):
    pass

class Methanomicrobiales(Archaea):
    pass

class ExtremeHalophiles(Archaea):
    pass


#Eucarya Subclasses
class Animalia(Eucarya):
    pass

class Fungi(Eucarya):
    pass

class Plantae(Eucarya):
    pass

class Ciliates(Eucarya):
    pass

class Flagellates(Eucarya):
    pass

class Microsporidia(Eucarya):
    pass


#Example
b = Thermotoga("BacName")
b.display()
print(b)
