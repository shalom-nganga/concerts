class Concert:
    all = []
    def __init__(self, band,date, venue) :
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

        @property
        def band(self):
            return self.band
        
        def venue(self):
            return self.venue
        
