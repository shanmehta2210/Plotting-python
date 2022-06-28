Phonebook = [
    ["Name", 1238932923, "Works at Shreyansh Creations", False]
]

Phonebook_Descript = ["name", "number", "job", "favorite"]


def add_contact(name, number, job, favorite):
    Phonebook.append([name, number, job, favorite])


def find_thing(thing, col):
    i = 0
    for row in Phonebook:
        if row[col] == thing:
            return i

        i = i + 1


def Clear():
    Phonebook.clear()


def Convert():
    global Start_num, Target_num
    Target = input("Enter the value you want: ")
    Start = input("Enter the value you have: ")
    Value = input("enter the actual thing: ")

    i = 0
    for val in Phonebook_Descript:
        if val == Start:
            Start_num = i

        i = i + 1

    j = 0
    for valu in Phonebook_Descript:
        if valu == Target:
            Target_num = j

        j = j + 1

    return Phonebook[find_thing(Value, Start_num)][Target_num]


def remove_row():
    global col_num
    field = input("Enter the value you have: ")
    row_to_remove = input("enter the actual thing: ")

    i = 0
    for val in Phonebook_Descript:
        if val == field:
            col_num = i

        i = i + 1

    Phonebook.remove(Phonebook[find_thing(row_to_remove, col_num)])


def print_phonebook():
    for i in range(len(Phonebook)):
        print(Phonebook[i])


def show_favorites():
    Favorites_shown = []
    i = 0
    for row in Phonebook:
        if row[3]:
            Favorites_shown.append(Phonebook[i])
        i = i + 1

    for d in range(len(Favorites_shown)):
        print(Favorites_shown[d])



print("Welcome to the BEST PHONEBOOK\nShan Phonebook")
print("Press a to add a new contact\nPress b to get a value from giving another\nPress c to remove a row")
print("Press d to show all your favorites\nPress e to print the entire phonebook")
print("And I advise you not to do this but you can also press f to clear the entire phonebook")

for i in range(1, 1000):
    choice = input("So, what do you choose: ")

    if choice == "a":
        name = input("Enter the name: ")
        number = input("Enter their number: ")
        occupation = input("Enter what they do: ")
        favorite = input("If you want them to be in your favorites, enter True, and if not enter False(be careful of the "
                         "capitalisation)")
        add_contact(name, number, occupation, favorite)
        fer = input("done. Would you like to perform another operation, type a if yes and b if no")
        if fer == "a":
            continue
        else:
            break
    elif choice == "b":
        print("you will have to provide the field that you wish to get information about, for ex if you wanted to ask about "
              "suresh's job, field one would be 'name', field two would be the field you desire, i.e, 'job', and then you w"
              "ould write the name, i.e, Suresh")
        va = Convert()
        print("The demanded info is " + va)
        fer = input("Would you like to perform another operation, type a if yes and b if no")
        if fer == "a":
            continue
        else:
            break
    elif choice == "c":
        print("You can provide the field of your info, and also the value itself, for ex, if you wanted to delete the ro"
              "w with name 'Suresh', you would write name in field and Suresh in value, or similarly write the number as"
              "field if you wanted to delete the row with number 9822353380")
        remove_row()
        print("Row removed")
        fer = input("Would you like to perform another operation, type a if yes and b if no")
        if fer == "a":
            continue
        else:
            break
    elif choice == "d":
        print("This will show all your favorites")
        show_favorites()
        fer = input("Would you like to perform another operation, type a if yes and b if no")
        if fer == "a":
            continue
        else:
            break
    elif choice == "e":
        print("This will print the entire phonebook")
        print_phonebook()
        fer = input("Would you like to perform another operation, type a if yes and b if no")
        if fer == "a":
            continue
        else:
            break
    elif choice == "f":
        print("Are you incredibly sure you wish to do this? This will delete your entire notebook up to this point.")
        check = input("Type a if you are sure, and b if you wanna turn back")
        if check == "a":
            Clear()
            fer = input("Would you like to perform another operation, type a if yes and b if no")
            if fer == "a":
                continue
            else:
                break
        elif check == "b":
            continue




#stuff = Convert()

#show_favorites()
#print(stuff)
