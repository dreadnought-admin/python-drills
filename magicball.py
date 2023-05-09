import time
import random
import sys

# question = input(("Welcome, wayward soul. Ask the Magic 8 Ball a Question and Learn Your Future: \n"))
responses = [  
    "It is certain",   
    "It is decidedly so",    
    "Without a doubt",    
    "Yes – definitely",    
    "You may rely on it",    
    "As I see it, yes",    
    "Most likely",    
    "Outlook good",    
    "Yes",    
    "Signs point to yes",    
    "Reply hazy, try again",   
    "Ask again later",    
    "Better not tell you now",    
    "Cannot predict now",    
    "Concentrate and ask again",    
    "Don't count on it",    
    "Outlook not so good",    
    "My sources say no",    
    "Very doubtful",    
    "My reply is no"]

choice_index = random.randint(0, len(responses)-1)
result = responses[choice_index]

def magic_ball():
    question = input(("Welcome, wayward soul. Ask the Magic 8 Ball a Question and Learn Your Future: \n"))
    player_question = str(question)
    if len(player_question) > 0:
        print(result)
        play_again = input(("Do you want to play again? Press 'Y' for 'Yes' or 'X' to exit \n")).capitalize()
        if play_again == "Y":
            magic_ball()
        elif play_again == "X":
            print("Goodbye.")
            sys.exit(-1)
    else:
        print("You have to ask a question to get a response.")

magic_ball()
