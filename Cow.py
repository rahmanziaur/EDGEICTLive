class Cow:

    def __init__(self):
        self.cowDict = {}

    def updateDict(self, name, location):
        self.cowDict.update({name: location})

    def view(self):
        print(self.cowDict)
        #print("Location:", self.locationList)