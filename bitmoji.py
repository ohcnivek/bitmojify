#!/usr/bin/env python
import os.path
import random
from datetime import date
from pprint import pprint
import requests
import holidays
import subprocess
import urllib.request

# RUNNING & GENERATING: index.js and getting the link from the output
encoding = 'utf-8'
output = subprocess.check_output("node index.js", shell=True)
strLinkToBitmoji = str(output, encoding)

f = open('generatedLibmoji.jpg', 'wb')
f.write(urllib.request.urlopen(strLinkToBitmoji).read())
f.close()


# for holidays
today = date.today()
print("Today's date:", today)  # format: 2020-07-18
dateStringRepresentation = str(today)
# dateStringRepresentation = "2020-07-04" // TEST for checking validity

year = dateStringRepresentation[0:4]
month = dateStringRepresentation[5:7]
day = dateStringRepresentation[8:]
us_holidays = holidays.UnitedStates()

# https://covidtracking.com/data/api
# covid api access START
state = input("Enter your state's 2 letter abbreviation: ")
state = state.lower()
api_address = 'https://covidtracking.com/api/v1/states/' + state + '/current.json'
json_data = requests.get(api_address).json()
pprint(json_data)
# covid api access END

# creating myresume.tex / reading skeleton.tex
filename = "myresume"
opfile = filename + '.tex'
outfile = open(opfile, 'w')
readfile = open("skeleton.tex", 'r')  # reading from the resume file
toAdd = readfile.readlines()

# cumulative list of names
listOfImageNames = ['check', 'rain', 'mask']


def a_tex_file():
    substring = "check"  # this is the default bitmoji in skeleton.tex
    for i in toAdd:
        if substring in i:  # looking for where substring "check" is so it can replace it
            i = image_determinant(i)
        outfile.writelines(i)
    outfile.close()


def image_determinant(i):
    index = random.randrange(2)
    if date(int(year), int(month), int(day)) in us_holidays:
        holidayName = us_holidays.get(dateStringRepresentation)
        print(holidayName)
        #adjust for the different holidays here
    #TODO adjust this method for the spacing and scaling too if im using the default and not the randomly generated bitmoji

    # elif json_data['deathIncrease'] > 15:
    #     print("Cases are still increasing!!")
    #     i = i.replace("check", listOfImageNames[2])  # changing the image to the masked bitmoji
    #     print("this is the image used: " + listOfImageNames[2])
    else:
        i = i.replace("check", 'generatedLibmoji')
        print("this is the image used: " + 'generatedLibmoji')
    return i


a_tex_file()


# automatically compiles with updated pdf file
os.system("pdflatex myresume.tex")


