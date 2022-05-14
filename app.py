from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from gptg import gpt_search
from text import *
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    body = request.values.get('Body').lower()
    # Start our TwiML response
    resp = MessagingResponse()
    command = body.split()[0]
    if " " in body:
        prompt = body.split(' ', 1)[1]
    elif body == "commands":
        resp.message(commands_string)
    else:
        resp.message("ERROR you only typed one word" + commands_string)
    
    if command == "transit":
        resp.message("You inputed TRANSIT command")
    elif command == "general":
        prompt = body.split(' ', 1)[1]
        prompt = prompt + ":"
        resp.message(gpt_search(prompt))
    elif command == "weather":
        resp.message("You inputed WEATHER command")
    elif command == "commands":
        resp.message(commands_string)
    else:
        resp.message("Please type either TRANSIT, GENERAL or WEATHER in front of your inquires! Type COMMANDS for a list of commands")
    

    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)