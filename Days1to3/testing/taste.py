#ask the user thier name
name = input("What is your name? ")

#ask their favorite food
favFood = input("What is your favorite food? ")

#evaluate if they have good taste
def taste(name, favFood):
    if favFood == "fries":
        return "Hello " + name + " you taste in food is fire."
        
    elif favFood == "mashpotatoes":
            return "Hello " + name + " you taste in food is fire."
    else:
            "Hello " + name + " you have trash taste in food."
            
print(taste(name, favFood))