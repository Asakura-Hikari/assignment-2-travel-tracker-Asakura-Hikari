"""..."""

# Create your PlaceCollection class in this file
import operator

from place import Place


class PlaceCollection:
    """Create a class to read files"""

    def __init__(self, places=None):
        """create a place list to help collection"""
        if places is None:
            places = []
        self.places = places

    def __str__(self):
        """Create an initial output"""
        test_place = ""
        for place in self.places:
            test_place += str(print(place)) + '\n'
        return test_place

    def load_places(self, file_name):
        """Load place information from csv to list, return a place list"""
        file = open(file_name, "r")
        content = file.readlines()  # read the whole file
        for i in content:
            place = i.strip('\n').split(',')
            if place[3] == 'v':
                new_place = Place(place[0], place[1], place[2], True)
                self.places.append(new_place)
            elif place[3] == 'n':
                new_place = Place(place[0], place[1], place[2], False)
                self.places.append(new_place)
        file.close()

    def save_places(self):
        """Save the list into csv file"""
        file = open("places.csv", "w")
        for place in self.places:  # write list into file
            if place.visit:
                file.write("{},{},{},{}\n".format(place.name, place.country, place.priority, 'v'))
            elif not place.visit:
                file.write("{},{},{},{}\n".format(place.name, place.country, place.priority, 'n'))

    def add_place(self, place):
        """Add a new place into list"""
        self.places.append(place)

    def get_num_of_unvisited(self):
        """return a unvisited number"""
        unvisited_num = 0
        for place in self.places:
            if not place.visit:
                unvisited_num += 1
        return unvisited_num

    def sort(self, way):
        """sort places list"""
        if way == 'PRIORITY':
            self.places = sorted(self.places, key=lambda place: (place.visit, int(place.priority)))
        if way == 'COUNTRY':
            self.places = sorted(self.places, key=lambda place: (place.visit, place.country))
        if way == 'NAME':
            self.places = sorted(self.places, key=lambda place: (place.visit, place.name))
