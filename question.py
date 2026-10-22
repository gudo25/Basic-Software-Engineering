from node import Node


class Question(Node):
    def __init__(self, question, yes_node, no_node):
        self.str = question
        self.yes_node = yes_node
        self.no_node = no_node
        #self.is_question = True
    #def get_question(self):
    #    return self.question
    