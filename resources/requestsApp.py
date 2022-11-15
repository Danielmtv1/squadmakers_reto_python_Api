from flask import jsonify
import requests
import json
from math import lcm as mcm
from functools import reduce
import random

# the function an other Requests for Apps

# get joke for chucknorris api
def chuckNorrisJoke():

    url = "https://api.chucknorris.io/jokes/random"
    data = requests.get(url)

    if data.status_code == 200:
        data = data.json()
        str_json = json.dumps(data)
        dic_json = json.loads(str_json)
        jokeChuckNorris = dic_json["value"]
        return jokeChuckNorris


# get joke for dadjoke api
def dadJoke():
    url = "https://icanhazdadjoke.com/slack"
    data = requests.get(url)

    if data.status_code == 200:
        data = data.json()
        for e in data["attachments"]:
            dadJokest = e["text"]
            return dadJokest


# this a definition mathematical for mcm
def mcm(a, b):
    a = int(a)
    b = int(b)

    if a > b:
        greaterThan = a
    else:
        greaterThan = b

    while True:
        if greaterThan % a == 0 and greaterThan % b == 0:
            mcm = greaterThan
            break
        greaterThan += 1

    return mcm


# use for mcm in a list
def mcm_for(listNumbers):
    return reduce(lambda x, y: mcm(x, y), listNumbers)


# use for util list get by  param
def comma_separated_params_to_list(param):
    result = []
    for val in param.split(","):
        if val:
            result.append(val)
    return result


# this function use random for get joke of chuck norris or dad
def RandomJokes():
    randomChoice = random.randint(1, 2)
    if randomChoice == 2:
        chuckNorrisJokes = chuckNorrisJoke()
        return chuckNorrisJokes

    if randomChoice == 1:
        dadJokes = dadJoke()

        return dadJokes
