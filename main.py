from os import system

import question
import animal

def main():
    stop = False
    base_node = question.Question("Does it swim?", animal.Animal("Seal"), animal.Animal("Bird"))
    print("Animal Guesser...")
    current_node = base_node
    prev_node = base_node
    prev_answer = False
    while not stop:
        print(current_node.get_string())
        choice = input("yes / no --> ")

        #if choice == "q":
        #    print("Bye, bye!")
        #    stop = True

        if choice.lower() == "yes":
            tmp_node = current_node.answer(True)
            if(tmp_node is current_node):
                print("The animal you thought of was: ", current_node.get_string())
                current_node = base_node
                system("clear||cls")
                print("game restarted")
                prev_answer = False
            else:
                prev_node = current_node
                current_node = tmp_node
            prev_answer = True

        elif choice.lower() == "no":
            tmp_node = current_node.answer(False)
            if(tmp_node is None):
                print("The animal you thought of is not in my memory: ")
                in_animal_name = input("What animal were you thinking about: ")
                in_new_question = input(f"Please type in a question that would distinguish a {current_node.get_string()} from a {in_animal_name}: ")
                new_tmp_node = question.Question(in_new_question, animal.Animal(in_animal_name),current_node)
                prev_node.insert(prev_answer,new_tmp_node)
                current_node = base_node
                system("clear||cls")
                print("game restarted")
                prev_answer = False
            else:
                prev_node = current_node
                current_node = tmp_node
            prev_answer = False

        elif choice.lower() == "q":
            stop = True

        base_node

if __name__ =="__main__":
    main()