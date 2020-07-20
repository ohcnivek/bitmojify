#!/usr/bin/env python
import os.path
from datetime import date
from pprint import pprint
import requests
import holidays
import subprocess
import urllib.request

encoding = 'utf-8'
output = subprocess.check_output("node index.js", shell=True)
strLinkToBitmoji = str(output, encoding)
f = open('generatedLibmoji.jpg', 'wb')
f.write(urllib.request.urlopen(strLinkToBitmoji).read())
f.close()

today = date.today()  # format: 2020-07-18
dateStringRepresentation = str(today)
year = dateStringRepresentation[0:4]
month = dateStringRepresentation[5:7]
day = dateStringRepresentation[8:]
us_holidays = holidays.UnitedStates()

# https://covidtracking.com/data/api
state = input("Enter your state's 2 letter abbreviation: ")
state = state.lower()
api_address = 'https://covidtracking.com/api/v1/states/' + state + '/current.json'
json_data = requests.get(api_address).json()
pprint(json_data)

# creating myresume.tex / reading skeleton.tex
filename = "myresume"
opfile = filename + '.tex'
outfile = open(opfile, 'w')
readfile = open("skeleton.tex", 'r')  # reading from the resume file
toAdd = readfile.readlines()

# cumulative list of names
#TODO add holiday bitmojis here
listOfImageNames = ['check', 'rain', 'mask']


def a_tex_file():
    substring = "check"
    for i in toAdd:
        if substring in i:
            print("found found found found found")
            i = image_determinant(i)
        outfile.writelines(i)
    outfile.close()


def image_determinant(i):
    if date(int(year), int(month), int(day)) in us_holidays:
        holidayName = us_holidays.get(dateStringRepresentation)
        print(holidayName)
    elif json_data['deathIncrease'] > 25:
        i = i.replace("480,645", "450,680")
        i = i.replace("scale = .14", "scale = .25")
        i = i.replace("check", listOfImageNames[2])
        print("this is the image used: " + listOfImageNames[2])
    else:
        i = i.replace("check", 'generatedLibmoji')
        print("this is the image used: " + 'generatedLibmoji')
    return i


a_tex_file()


# automatically compiles with updated pdf file
os.system("pdflatex myresume.tex")


