VINTAGE_YEAR = 50


class Guitar():

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of a guitar"""
        return "{} ({}) : {:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return year of guitar made"""
        return YEAR = self.year

    def is_vintage(self):
        """Determine whether the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_YEAR

    
