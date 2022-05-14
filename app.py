from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from gpt import gpt_search
from text import *
from transit_test import get_transit
from weather import weather_city
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    body = request.values.get('Body').lower()
    if(not body):
        resp.message("I'm not quite sure what you mean.\n" + commands_string)

    # Start our TwiML response
    resp = MessagingResponse()
    command = body.split()[0]

    # If there are more than 2 words in the body
    if " " in body:
        prompt = body.split(' ', 1)[1]
        prompt = prompt.strip()
        if(not prompt):
            resp.message("Make sure to type something after your commands!\nType COMMANDS for a list of commands ")
        elif command == "transit":
            resp.message("\n" + get_transit(prompt))
        elif command == "general":
            prompt = prompt + ":"
            resp.message("\n" + gpt_search(prompt))
        elif command == "weather":
            # city = input("Enter the Name of City ->  ")
            # city = city+" weather"
            resp.message("\n" + weather_city(prompt))
            # resp.message("You inputed WEATHER command")
        elif command == "commands":
            resp.message(commands_string)
        else:
            resp.message("\nPlease type either TRANSIT, GENERAL or WEATHER in front of your inquires! Type COMMANDS for a list of commands")
    
    # If there is only 1 word in the body and it is command
    elif body == "commands":
        resp.message(commands_string)
    
    # If they only typed one word in the body
    else:
        resp.message("ERROR you only typed one word" + commands_string)

    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)