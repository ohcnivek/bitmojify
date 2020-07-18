#!/usr/bin/env python
import os.path
import random
from datetime import date
from pprint import pprint
import requests
import holidays

# for holidays, sporting events
today = date.today()
print("Today's date:", today)  # format: 2020-07-18
dateStringRepresentation = str(today)
# dateStringRepresentation = "2020-07-04" // for checking validity

year = dateStringRepresentation[0:4]
month = dateStringRepresentation[5:7]
day = dateStringRepresentation[8:]
us_holidays = holidays.UnitedStates()
print(year)
print(month)
print(day)

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
        #adjust for all the holidays here
    # elif json_data['deathIncrease'] > 15:
    #     print("Cases are still increasing!!")
    #     i = i.replace("check", listOfImageNames[2])  # changing the image to the masked bitmoji
    #     print("this is the image used: " + listOfImageNames[2])
    else:
        i = i.replace("check", listOfImageNames[index])
        print(index)
        print("this is the image used: " + listOfImageNames[index])
    return i


a_tex_file()


# automatically compiles pdf file for you
os.system("pdflatex myresume.tex")

# os.system('tex '+ opfile)
# os.system('xdvi ' + filename + '.dvi & ')
