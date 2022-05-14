from weather import weather_city
from gpt import gpt_search
from text import *
from transit_test import get_transit


body = input("Enter your command: ")
def test(body):
    if(not body):
        return ("I'm not quite sure what you mean.\n" + commands_string)
    body = body.lower()
    command = body.split()[0]

    # If there are more than 2 words in the body
    if " " in body:
        prompt = body.split(' ', 1)[1]
        prompt = prompt.strip()
        if(not prompt):
            return("Make sure to type something after your commands!\nType COMMANDS for a list of commands ")
        elif command == "transit":
            return("\n" + get_transit(prompt))
        elif command == "general":
            prompt = prompt + ":"
            return("\n" + gpt_search(prompt))
        elif command == "weather":
            # city = input("Enter the Name of City ->  ")
            # city = city+" weather"
            return ("\n" + weather_city(prompt))
            # resp.message("You inputed WEATHER command")
        elif command == "commands":
            return (commands_string)
        else:
            return ("\nPlease type either TRANSIT, GENERAL or WEATHER in front of your inquires! Type COMMANDS for a list of commands")
    
    # If there is only 1 word in the body and it is command
    elif body == "commands":
        return(commands_string)
    
    # If they only typed one word in the body
    else:
        return ("I'm not quite sure what you mean.\n" + commands_string)
    

print(test(body))