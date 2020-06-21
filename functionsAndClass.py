# Functions
# def [functionName] (someparms,....):
    #[executable code block]

# def [functionName](someParm: data Type, ...) -> returnType:
    # [exeucutable code bock]

def printString(someString): # Does not return a value
    print(someString)

def printStringTypehints(someString: str) -> None:
    print(someString)

def returnString(someString: str) -> str:
    return someString

someListofInts = [55,22,11,33,44,10,93]

def calculateMean (someList) -> float:
    summator = 0
    for number in someList:
        summator = summator + number
    return summator / len(someList)

print(calculateMean(someListofInts))

# Classes are objects that have attributes and methods associated with its definition

class Animal():

    def __init__(self, animalType):
        self.animalType = animalType
    
    def printAnimalType(self):
        print(self.animalType)
    
parrot = Animal("Parrot")
parrot.printAnimalType()

dog = Animal("Dog")
dog.printAnimalType()

class Mammal(Animal):

    def __init__(self, animalType: str,  hasFur: bool) -> None:
        self.animalType = animalType
        self.hasFur = hasFur
    
    def isAFurryMammal(self) -> None:
        if self.hasFur:
            print("Furry Mammal")
        else:
            print("Hairless")

regularCat = Mammal("regular furry cat", True)
print(regularCat.animalType)
print(regularCat.hasFur)
regularCat.hasFur()




