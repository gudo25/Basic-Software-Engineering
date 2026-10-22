from node import Node

class Animal(Node):
    def __init__(self, animalName):
        self.str = animalName
        #self.is_question = False

    #def get_question(self):
    #    return self.animal_name
    def answer(self, theAnswer):
        if(theAnswer == True):
            return self
        else:
            return None