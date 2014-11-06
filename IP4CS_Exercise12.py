# In Class Exercise 12
# Classes - object oriented programming
# author: jiinso
# date: 10/23/2014

# create a class "Animal"
class Animal:

    # define attributes
    country = "Kenya"
    label = "Animals Found in Kenyan Safari"
    
    # define attributes that should be input initially with an instance
    def __init__(self, name, age, weight, species):
        self.name = name
        self.age = age
        self.weight = weight
        self.species = species



class Dogs(Animal):
    type = "mammal"
    order = "Carnivora"
    suborder = "Caniformia"
    family = "Canidae"
    

hippo = Animal("Hippo", "12", "1500", "Hippopotamus amphibius")
girrafe = Animal("Girrafe", "3", "800", "Giraffa camelopardalis")
elephant = Animal("Elephant", "50", "6000", "Loxodonta africana")
rhino = Animal("Rhinoceros", "20", "1200", "Diceros bicornis")

jackal = Dogs("Golden jackel", "9", "30", "Canis aureus")
wilddog = Dogs("African wild dog", "2", "18", "Lycaon pictus")

print wilddog


