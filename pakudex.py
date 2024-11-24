#Vivian Li
#COP3504C
from pakuri import Pakuri
import math

class Pakudex:
    def __init__(self):
        self.species_list = list() #strings
        self.pakuri_list = list() #pakuris

    def get_species_list(self): #returns list of names (strings)
        if len(self.species_list) == 0:
            return None
        return self.species_list

    def get_stats(self, species): #returns intlist with level, cp, and hp
        if species not in self.species_list:
            return None
        intlist = list()
        index = self.species_list.index(species)
        kuri = self.pakuri_list[index]
        intlist.append(kuri.level) #adding level to 0 index
        cp = kuri.cp
        intlist.append(cp)
        hp = kuri.hp
        intlist.append(hp)
        return intlist

    def sort_pakuri(self):
        self.species_list.sort()
        for i in range(len(self.species_list)): #for every index in strings list
            for num in range(len(self.pakuri_list)): #for every index in pakuri list
                if self.pakuri_list[num].get_species() == self.species_list[i]:
                    popped_pak = self.pakuri_list.pop(num) #remove from og location
                    self.pakuri_list.insert(i,popped_pak) #insert in new loc

    def add_pakuri(self, species, level):
        if species not in self.species_list:
            kuri = Pakuri(species, level) #makes new pakuri
            self.pakuri_list.append(kuri) #adds pakuri to pakudex
            self.species_list.append(species) #adds species name to species list
            return True
        else:
            return False

    def remove_pakuri(self, species):
        if species in self.species_list:
            index = self.species_list.index(species) #index of the species in the name list, should correspond with object list
            self.pakuri_list.pop(index) #should correspond, removes object from object list
            self.species_list.remove(species) #removes species name from string list
            # self.pakuri_list.remove(species) #how to remove object from list?
            return True
        else:
            return False

    def evolve_species(self, species):
        if species in self.species_list:
            pakuri_index = self.species_list.index(species)
            pak = self.pakuri_list[pakuri_index]
            pak.set_attack(pak.get_attack()+1)
            pak.level=pak.level*2
            return True
        return False

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!\n")
    paku = Pakudex()
    option = 0
    while option != 7:
        print("Pakudex Main Menu")
        print("-----------------")
        print("""1.\tList Pakuri
2.\tShow Pakuri
3.\tAdd Pakuri
4.\tRemove Pakuri
5.\tEvolve Pakuri
6.\tSort Pakuri
7.\tExit""")
        try:
            option = int(input("\nWhat would you like to do? "))
            if option == 1: #list pakuri
                species_list = paku.get_species_list()
                if species_list is None:
                    print("\nNo Pakuri currently in the Pakudex!")
                else:
                    i = 1
                    print('\nPakuri in Pakudex:')
                    for item in species_list:
                        print(str(i) + '.', item)
                        i += 1
                print()
            elif option == 2: #show pakuri
                print("\nEnter the name of the species to display: ", end='')
                species = input()
                intlist = paku.get_stats(species)
                if intlist is None:
                    print("Error: No such Pakuri!\n")
                else:
                    print("\nSpecies:", species)
                    print("Level:", intlist[0])
                    print("CP:", intlist[1])
                    print("HP:", intlist[2], '\n')
            elif option == 3: #add pakuri
                s = input("\nSpecies: ")
                specieslist = paku.get_species_list()
                if specieslist != None and s in specieslist:
                    print("Error: Pakudex already contains this species!\n")
                    continue
                success = False
                while True:
                    try:
                        while True:
                            l = int(input("Level: "))
                            if l < 0:
                                print("Level cannot be negative")
                            else:
                                success = True
                                break
                    except:
                        print("Invalid Level!")
                    if success:
                        break

                if paku.add_pakuri(s, l) == True:
                    print("Pakuri species", s, "(level", str(l) +  ") added!\n")

            elif option == 4: #remove pakuri
                s = input("\nEnter the name of the Pakuri to remove: ")
                if paku.remove_pakuri(s) == True:
                    print("Pakuri", s, "removed.\n")
                else:
                    print("Error: No such Pakuri!\n")
            elif option == 5: #evolve pakuri
                s = input("\nEnter the name of the species to evolve: ")
                if paku.evolve_species(s) == True:
                    print(s, "has evolved!\n")
                else:
                    print("Error: No such Pakuri!\n")
            elif option == 6: #sort pakuri
                paku.sort_pakuri()
                print("\nPakuri have been sorted!\n")
            elif option == 7: #exit
                print("\nThanks for using Pakudex! Bye!")
            else:
                print("\nUnrecognized menu selection!\n")
        except ValueError:
            print("\nUnrecognized menu selection!\n")
if __name__ == '__main__':
    main()