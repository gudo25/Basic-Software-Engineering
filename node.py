class Node:
    
    def __init__(self, data_string, yesNode = None, noNode = None):
        self.yes_node = yesNode
        self.no_node = noNode
        self.str = data_string
    def get_string(self):
        return self.str
    def answer(self,theAnswer):
        if(theAnswer == True):
            return self.yes_node
        else:
            return self.no_node
    def insert(self, theAnswer, newNode):
        if(theAnswer == True):
            self.yes_node = newNode
        else:
            self.no_node = newNode