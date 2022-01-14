import random

class CharacterGen:

    #initializations
    def __init__(self):
        self.classList = []
        self.raceList = []
        self.backgroundList = []
        self.finalCharacter = []
        pass
        
    def loadLists(self):
        playerClasses = open(r"./textFiles/Classes.txt","r")
        playerRaces = open(r"./textFiles/Races.txt","r")
        playerBackgrounds = open(r"./textFiles/Backgrounds.txt","r")
        
        for pc in playerClasses:
        
            self.classList.append(pc)
            
        for pr in playerRaces:
        
            self.raceList.append(pr)
            
        for pb in playerBackgrounds:

            self.backgroundList.append(pb)
            
        
    def buildCharacter(self):
        
        self.finalCharacter.append(self.raceList[random.randint(0, len(self.raceList) - 1)])
        self.finalCharacter.append(self.classList[random.randint(0, len(self.classList) - 1)])
        self.finalCharacter.append(self.backgroundList[random.randint(0, len(self.backgroundList) - 1)])
        
    
    
    def main(self):
        
        self.loadLists()
        self.buildCharacter()
        
        print("You could play a\n" + self.finalCharacter[0] + self.finalCharacter[1] + "with the " + self.finalCharacter[2] + " background", end='')



Object = CharacterGen()
Object.main()