from pakudex import Pakudex as dex

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    cap = -1
    while cap < 1:
        try:
            cap = int(input("Enter max capacity of the Pakudex: "))
            if cap < 1:
                print("Please enter a valid size.")
        except:
            print("Please enter a valid size.")
    
    creatures = dex(cap)
    print(f"The pakudex can hold {cap} species of Pakuri.")

    while True:
        choice = -1
        while choice < 1:
            try:
                choice = int(input(f"\nPakudex Main Menu\n{'-' * 17}\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit\n\nWhat would you like to do? "))
                if choice < 1:
                    print("Unrecognized menu selection!")
            except:
                print("Unrecognized menu selection!")

        match choice:
            case 1:
                if creatures.get_species_array():
                    print("Pakuri In Pakudex:")

                    for count, pakuri in enumerate(creatures.get_species_array(), 1):
                        print(f"{count}. {pakuri}")
                else:
                    print("No Pakuri in Pakudex yet!")
            case 2:
                species = input("Enter the name of the species to display: ")

                if creatures.get_stats(species):
                    stats = creatures.get_stats(species)

                    print(f"\nSpecies: {species}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}")
                else:
                    print("Error: No such Pakuri!")
            case 3:
                if creatures.get_size() == cap:
                    print("Error: Pakudex is full!")
                else:
                    species = input("Enter the name of the species to add: ")

                    print(f"Pakuri species {species} successfully added!") if creatures.add_pakuri(species) else print("Error: Pakudex already contains this species!")
            case 4:
                species = input("Enter the name of the species to evolve: ")

                print(f"{species} has evolved!") if creatures.evolve_species(species) else print("Error: No such Pakuri!")
            case 5:
                creatures.sort_pakuri()
                print("Pakuri have been sorted!")
            case 6:
                print("Thanks for using Pakudex! Bye!")
                exit()
            case _:
                print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()