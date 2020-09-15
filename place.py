"""
Name: Chaoyu Sun
Date started: 10/September/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-2-travel-tracker-Asakura-Hikari
"""


# Create your Place class in this file


class Place:
    """Create the place class"""
    # place_num = 0

    def __init__(self, name="", country="", priority=0, visit=False):
        """Create a constructor"""
        self.name = name
        self.country = country
        self.priority = priority
        self.visit = visit
        # self.place_num += 1

    def __str__(self):
        """Create an initial output"""
        if not self.visit:
            return "{} in {} priority {}".format(self.name, self.country,
                                                 self.priority)
        else:
            return "{} in {} priority {} (visited)".format(self.name, self.country,
                                                 self.priority)

    def make_visited(self):
        """Change place to visited"""
        self.visit = True

    def make_unvisited(self):
        """Change place to unvisited"""
        self.visit = False

    def is_important(self):
        """Determine if a place has a priority <= 2"""
        if self.priority <= 2:
            return True
        else:
            return False
