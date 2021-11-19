import requests
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
    #table_with_food = table_with_food[table_with_food.find("<table>"):table_with_food.find("</table>")]
    return table_with_food


def femza():
    r = requests.get("https://fe.uni-lj.si/o_fakulteti/restavracija/tedenski_meni/",verify=False)
    mainBody = r.text
    mainBody = mainBody[mainBody.find("<body"):mainBody.find("</body")]
    temporarySearchalg = mainBody# [mainBody.find('cnt-1808'):mainBody.find("</div>",mainBody.find('cnt-1808'))]
    datum = dt.now().strftime("%d.%m.%Y")
    dan = day_of_the_week[dt.now().strftime("%A")]
    temporarySearchalg = temporarySearchalg[temporarySearchalg.find("<table",temporarySearchalg.find(dan)):temporarySearchalg.find("</table>",temporarySearchalg.find(dan))]
    temporarySearchalg = temporarySearchalg.split("<tr>")[1:]
    i = 0
    for i in len(temporarySearchalg):
        temporarySearchalg[i] = temporarySearchalg[i].strip("</tr>").strip("</td>")
    
    print(temporarySearchalg)
    print(len(temporarySearchalg))
    # table_with_food = temporarySearchalg.split("<br />")[1:]
    #table_with_food = table_with_food[table_with_food.find("<table>"):table_with_food.find("</table>")]
    return 0
    
print(femza())

