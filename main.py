"""
Name: Chaoyu Sun
Date: 15/9/2020
Brief Project Description:
GitHub URL: https://github.com/JCUS-CP1404/assignment-2-travel-tracker-Asakura-Hikari
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

from place import Place
from placecollection import PlaceCollection


class TravelTrackerApp(App):
    """..."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')

    def build(self):
        self.title = "Travel Tracker"
        self.root = Builder.load_file('app.kv')
        self.create_list()
        return self.root

    def get_name(self):
        try:
            value = str(self.root.ids.input_name.text)
            return value
        except ValueError:
            return ''

    def get_country(self):
        try:
            value = str(self.root.ids.input_country.text)
            return value
        except ValueError:
            return ''

    def get_priority(self):
        try:
            value = int(self.root.ids.input_priority.text)
            return value
        except ValueError:
            return 0

    def get_sort(self):
        try:
            value = str(self.root.ids.input_sort.text)
            return value.upper()
        except ValueError:
            return ''

    def add_place(self):
        new_Place = Place(self.get_name(), self.get_country(), self.get_priority())
        if self.get_name() == '':
            self.root.ids.show_text.text = "All fields must be completed"
            return
        elif self.get_country() == '':
            self.root.ids.show_text.text = "All fields must be completed"
            return
        elif self.get_priority() == 0:
            self.root.ids.show_text.text = "Please enter a valid number"
            return
        else:
            self.place_collection.add_place(new_Place)
            self.clear_all()
            self.create_list()

    def clear(self):
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""
        self.root.ids.show_text.text = ""

    def sort(self):
        self.place_collection.sort(self.get_sort())
        self.clear_all()
        self.create_list()

    def create_list(self):
        self.place_collection.sort(self.get_sort())
        self.root.ids.show_unvisited_num.text = "Place to visit: {}".format(self.place_collection.
                                                                            get_num_of_unvisited())
        for place in self.place_collection.places:
            if not place.visit:
                place_label = Button(text=str(place), id=place.name, background_color=(1, 0.61, 0.61, 1))
                place_label.bind(on_release=self.press_entry)
                self.root.ids.places_list.add_widget(place_label)
            else:
                place_label = Button(text=str(place), id=place.name)
                place_label.bind(on_release=self.press_entry)
                self.root.ids.places_list.add_widget(place_label)

    def press_entry(self, instance):
        for place in self.place_collection.places:
            if str(place) == instance.text and not place.visit:
                self.status_text = "You visited {}, Great travelling!".format(place.name)
                self.root.ids.show_text.text = self.status_text
                place.visit = True
                self.clear_all()
                self.create_list()
                self.root.ids.show_unvisited_num.text = "Place to visit: {}".format(self.place_collection.
                                                                                    get_num_of_unvisited())

            if str(place) == instance.text and place:
                self.status_text = "You need to visit {}. Get going!".format(place.name)
                self.root.ids.show_text.text = self.status_text
                place.visit = False
                self.clear_all()
                self.create_list()
                self.root.ids.show_unvisited_num.text = "Place to visit: {}".format(self.place_collection.
                                                                                    get_num_of_unvisited())

    def clear_all(self):
        """"""
        self.root.ids.places_list.clear_widgets()

    def on_stop(self):
        self.place_collection.save_places()


if __name__ == '__main__':
    TravelTrackerApp().run()
