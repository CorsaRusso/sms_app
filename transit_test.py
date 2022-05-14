from bs4 import BeautifulSoup
import requests
from text import *
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_transit(prompt):
    if '->' in prompt:
        start = prompt.split("->")[0]
        finish = prompt.split("->")[1]
        start = start.strip()
        finish = finish.strip()
        if(not start or not finish):
            return transit_error_string1
        return transit(start,finish)
    else:
        return transit_error_string2

def format_url(start, finish):
    start = start.replace(" ", "+")
    finish = finish.replace(" ", "+")
    return "https://www.google.com/search?q=bus+from+"+ start + "+to+" + finish
    

def transit(start, finish):
    url = format_url(start, finish)
    res = requests.get(url)
    # print("Searching... \n")
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(res.status_code)
    # lst = soup.find_all(class_="atOwb")
    directions = soup.find_all(class_ = "BNeawe")
    direction = directions[0].parent
    time = direction.find("span").text
    for span_tag in direction.findAll('span'):
        span_tag.replace_with('Public transit arrives at')
    directions = direction.find("div").text

    eta = "\nEstimated trip time: " + time
    return directions + eta
    
    # start = start.replace("+", " ")
    # finish = finish.replace("+", " ")
    # print(f"The time to travel from {start} to {finish} by bus is {lst[0].get_text()}")
    