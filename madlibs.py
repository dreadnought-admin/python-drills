
def mad_libs():
    print('Welcome to the Spartan Madlib, Soldier.\n')
    warrior_name = input(('What is your name, Spartan?\n')).capitalize()
    pronoun = input(("Do you go by 'he', 'she', or 'they'? \n ")).lower()
    possessive_pronoun = input(("Do you use 'his', 'her', or 'their'? \n")).lower()

    adjective_1 = input(('Enter an adjective: \n')).lower()
    adjective_2 = input(('Enter a second adjective: \n')).lower()
    adjective_3 = input(('Enter a third adjective: \n')).lower()
    adjective_4 = input(('Enter a fourth adjective: \n')).lower()
    adjective_5 = input(('Enter a fifth adjective: \n')).lower()
    city = input(("Enter a city (preferrably Greek) name: \n"))
    verb = input(("Enter a verb: \n")).lower()
    adverb = input(('Enter an adverb (ex: quickly, slowly, rarely, happily, silently): \n')).lower()

    if possessive_pronoun ==  'his' or possessive_pronoun == 'her' or possessive_pronoun == 'their':
        pass
    else: 
        print("Sorry, please enter 'his', 'her', or 'their' for the possessive pronoun.")
        mad_libs()
    if pronoun == 'he' or pronoun == 'she' or pronoun == 'they':
        pass
    else:
        print("Sorry, please either 'He', 'She', or 'They' for your pronoun")
        mad_libs()
    
    story = f"Once upon a time, there was a Spartan warrior named {warrior_name}.\n {pronoun.capitalize()} was known throughout ancient Greece for {possessive_pronoun} {adjective_1} bravery and {possessive_pronoun} {adjective_2} strength.\n One day, {warrior_name} was {verb} in a battle against {adjective_3} enemies.\n {pronoun.capitalize()} put on {adjective_4} armor and picked up {possessive_pronoun} weapons, ready to fight.\n During the battle, {warrior_name} showed prowess and courage. {warrior_name} fought {adverb} and eventually emerged victorious.\n After the battle, {warrior_name} was celebrated as a hero. {pronoun.capitalize()} returned home to {city} and lived the rest of {possessive_pronoun} life as a legend.\n"
    
    print(f'Title: The Mighty Spartan Warrior\n {story}')
    

mad_libs()