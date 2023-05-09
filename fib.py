bouncer = input(('Bouncer: "Welcome to Club Python. How old are you?\n'))

def age_check(age):
    x = int(age)
    if x >= 18 and x > 0:
        response = "Go right in"
        print(response)
    elif x < 18 and x > 0:
        response = "Sorry, you're too young"
        print(response)
    else:
        response = "That is not a valid number"
        print(response)
        
age_check(bouncer)
