import requests
from datetime import datetime as dt

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

print(marjetica())