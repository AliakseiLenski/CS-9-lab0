from Animal import Animal
class AnimalShelter:
    def __init__(self):
        self.animalShelter = {}
    def addAnimal(self, animal):
        if animal.species not in self.animalShelter:
            self.animalShelter[animal.species] = [animal]     
        else: 
            self.animalShelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        '''
        if animal exists remove it from the list
        '''
        if self.doesAnimalExist(animal) == True:
            self.animalShelter[animal.species].remove(animal)            

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        str1 = ''
        if species in self.animalShelter:
            speciesList = self.animalShelter[species]
            for animal in speciesList:
                str1 = str1 + animal.toString() + '\n'
        else:
            return str1
        return str1[:-1]
        


    def doesAnimalExist(self, animal):
        '''
        check if an element exists in a dictionary
        if the key exists in a dictionary
        key animal.species
        continue to check if an animal object exists in a list of these species
        '''
        if animal.species in self.animalShelter:
            if animal in self.animalShelter[animal.species]:
                return True
            else:
                return False
        else:
            return False

