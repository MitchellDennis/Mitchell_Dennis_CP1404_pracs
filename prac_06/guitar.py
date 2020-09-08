

YEAR = 2020
VINTAGE_AGE = 50

class Guitar:
    """guitar calss, stores year, name and cost"""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = YEAR - self.year
        return age

    def is_vintage(self):

        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False
