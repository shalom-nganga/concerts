class Band:
    all = []

    def __init__(self, name, hometown) :
        self.name = name
        self.hometown = hometown
        Band.all.append(self)
        
        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
            self._name = name

        @property
        def hometown(self):
            return self._hometown
        
        @classmethod
        def all(cls):
            return cls._all
        

    






# print("max has a C200")
# print(19)
# print("13 pro max")