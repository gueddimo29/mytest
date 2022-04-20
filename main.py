import json

from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api=Api(app)
#req=requests.get("")
# joueurs=json.load(req.content)
if __name__ == "__main__":
    app.run(debug=True)

# tester si le joueur est valide
joueur = [
    {
        "id": "01",
        "pseudonyme": "mahdios",
        "imatriculation": [
            "AUTO-500-02-ISSI",
            "AUTO-500-02-ISSI"
        ],
        "numclassement": "3",
        "couleurbille": "jaune"
    },
    {
        "id": "01",
        "pseudonyme": "mahdios",
        "imatriculation": [
            "AUTO-500-02-ISSI",
            "AUTO-500-02-ISSI"
        ],
        "numclassement": "3",
        "couleurbille": "jaune"
    }
]


def tester_joueur(joueurbille):
    # tester la couleur
    if tester_couleur(joueurbille.couleurbille):
        for x in joueurbille.imatriculation:
            if tester_imatriculation(x):
                return False
    else:
        return True
    return True


def tester_imatriculation(sequence):
    result = sequence.split('-')
    if firstvalide(result[0]) and secondvalide(result[1]) and thirdpart(result[2]) and isreversed(result[3]):
        return True
    else:
        return False


def tester_couleur(couleur):
    if couleur == "vert" or couleur == "rouge" or couleur == "bleu":
        return False
    else:
        return True


def firstvalide(premiere):
    # SEMI MECA MINI AUTO
    if premiere == "AUTO" or premiere == "SEMI" or premiere == "MECA" or premiere == "MINI":
        return True
    else:
        return False


def secondvalide(chifre_entrier):
    if len(chifre_entrier) == 3:
        if (int(chifre_entrier) % 10) == 0:
            return True
        else:
            return False
    else:
        return False


def thirdpart(chifre_entrier):
    if len(chifre_entrier) == 2:
        return True
    else:
        return False


def isreversed(normal_string):
    reversed_string = normal_string[::-1]
    print(reversed_string)
    if len(normal_string) == 4:
        if normal_string == reversed_string:
            return True
        else:
            return False
    else:
        return False


tester_imatriculation("AUTO-500-02-MATA")
