"""
Replace the contents of this module docstring with your own details
Name: Chaoyu Sun
Date started: 31/july/2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-travel-tracker-Asakura-Hikari
"""


# main() function is to open and save the file.
def main():
    print("Travel Tracker 1.0 - by Chaoyu Sun")
    print("3 places loaded from places.csv")
    file = open("places.csv", "r+")

    content = file.readlines()  # read the whole file
    place_list = []  # create a list to add every place
    for i in content:  # split one place to one list
        place = i.strip('\n').split(',')
        place_list.append(place)

    file.seek(0)  # reset file index to the beginning
    place_list = menu(place_list)

    for place in place_list:  # write list into file
        file.write("{},{},{},{}\n".format(place[0], place[1], place[2], place[3]))
    file.close()

    print("{} places saved to places.csv".format(len(place_list)))
    print("Have a nice day :)")


# menu() function is to loop the main menu.
def menu(place_list):
    var = True  # set quit value
    while var:
        place_list = sorted(place_list, key=lambda x: (x[3], int(x[2])))  # sort list

        print("Menu:")
        print("L - List places ")
        print("A - Add new place")
        print(" M - Mark a place as visit ")
        print("Q - Quit")
        select = input(">>> ").upper()  # get upper input value

        if select == 'L':
            list_places(place_list)

        elif select == 'A':
            place_list = add_new_place(place_list)

        elif select == 'M':
            place_list = mark_place(place_list)

        elif select == 'Q':
            return place_list

        else:
            print("Invalid menu choice")


# list_places is to list the places in menu.
def list_places(place_list):
    i = 0  # to count unvisited place number
    for place in place_list:
        i += 1
        if place[3] == 'n':  # printing depend visit and unvisited
            print("*{}. {:<15} in {:<15} priority {:<15}".format(i, place[0], place[1], place[2]))
        else:
            print(" {}. {:<15} in {:<15} priority {:<15}".format(i, place[0], place[1], place[2]))


# add_new_place is to add new places in list.
def add_new_place(place_list):
    new_place = []
    name = input("Name: ")
    while name == '':  # retry if name is blank
        print("Input can not be blank ")
        name = input("Name: ")
    new_place.append(name)

    country = input("Country: ")
    while country == '':  # retry if country is blank
        print("Input can not be blank ")
        country = input("Country: ")
    new_place.append(country)

    var = True  # create a support variable to help loop
    while var:
        try:  # retry if priority not a number
            priority = int(input("Priority: "))
        except ValueError:
            print("Invalid input, enter a valid number ")
            continue

        if priority < 0:  # retry if priority is a negative number
            print("Number must be > 0")

        else:
            new_place.append(priority)
            new_place.append("n")
            print("{} in {} (priority {}) added to Travel Tracker ".format(name, country, priority))

            place_list.append(new_place)  # add new place in list
            return place_list


# mark_place is to change place from unvisited to visit.
def mark_place(place_list):
    unvisited = 0
    for place in place_list:
        if place[3] == 'n':  # to check how many places are unvisited.
            unvisited += 1

    if unvisited == 0:  # if all places are unvisited, return the function.
        print("No unvisited places")
        return

    list_places(place_list)
    print("{} places. You still want to visit {} places.".format(len(place_list), unvisited))

    var = True
    while var:
        try:  # check if enter value not a number.
            print("Enter the number of a place to mark as unvisited ")
            mark = int(input(">>> "))
        except ValueError:
            print("Invalid input; enter a valid number")
            continue

        if mark < 0:  # check the number must large than 0.
            print("Number must be > 0")
        elif mark > len(place_list):  # check the number is valid number in place.
            print("Invalid place number")
        elif place_list[mark - 1][3] == 'v':  # check if this place are unvisited.
            print("That place is already unvisited")
        else:  # change place to unvisited successfully.
            place_list[mark - 1][3] = 'v'
            print("{} in {} unvisited!".format(place_list[mark - 1][0], place_list[mark - 1][1]))
            return place_list


if __name__ == '__main__':
    main()

