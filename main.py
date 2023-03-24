import requests
import pandas as pd
from datetime import datetime as dt

#Global Variables and Dictionaries
day_of_the_week = {
    "Monday":"ponedeljek",
    "Tuesday":"torek",
    "Wednesday":"sreda",
    "Thursday":"četrtek",
    "Friday":"petek",
    "Saturday":"sobota",
    "Sunday":"nedelja",
}

menu = dict()

# Functions
def marjetica():
    r = requests.get("https://marjetice.si/")
    mainBody = r.text
    mainBody = mainBody[mainBody.find("<body"):mainBody.find("</body")]
    temporarySearchalg = mainBody[mainBody.find('blogPost'):mainBody.find("</div>",mainBody.find('blogPost'))]
    datum = dt.now().strftime("%d.%m.%Y")
    temporarySearchalg = temporarySearchalg[(temporarySearchalg.find(datum)+ len( datum+"<strong>")+1):temporarySearchalg.find("</p>",temporarySearchalg.find(datum))]

    table_with_food = temporarySearchalg.split("<br />")[1:]
    for i in range(len(table_with_food)):
        table_with_food[i] = table_with_food[i].split(",")
    return table_with_food


def femza():
    table_with_food = pd.read_html('https://www.fe.uni-lj.si/o_fakulteti/restavracija/tedenski_meni/')
    datum = dt.now().strftime("%w")
    if int(datum) > 0:
        datum = int(datum) - 1
    else:
        datum = 6
    # print(datum)
    # print(table_with_food[datum])
    return table_with_food[datum]



print(marjetica())
print(femza())

