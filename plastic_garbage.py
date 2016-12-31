from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, is_clean):
        self.name = name
        self.is_clean = is_clean

    def cleaned(self):
        if self.is_clean == False:
            self.is_clean = True
        return self.is_clean
