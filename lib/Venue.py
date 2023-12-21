class Venue:

    all = []
    
    def __init__(self, title, city) :
        self._title = title
        self._city = city
        Venue.all.append(self)
        self.venue.concert.append(self)
        
        @property
        def title(self):
            return self._title
        
        @title.setter
        def title(self, title) :
            return self._title
