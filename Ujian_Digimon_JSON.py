from bs4 import BeautifulSoup
import requests

r = requests.get("http://digidb.io/digimon-list/")
soup = BeautifulSoup(r.content, 'html.parser')

dataTarget = soup.find_all('tr', class_='')
# print(dataTarget)
# print(len(dataTarget))                       
# print(dataTarget[:4433])
# print(dataTarget[0].img['src'])
# print(dataTarget[0].text[0])
# print(dataTarget[0].td.find_next_sibling())
# print(dataTarget[0].td.find_next().text)
# print(dataTarget[0].find_all('center')[0].text)
# print(len(dataTarget[0].find_all('center')))
# print(dataTarget[0].b.text.replace(' ',''))

dataJSON=[]
for i in range(len(dataTarget)):
    scrap=dataTarget[i]
    value=scrap.find_all('center')
    no=scrap.b.text.replace('\xa0','')
    digimon=scrap.a.text
    image=scrap.img['src']
    stage=value[0].text
    tipe=value[1].text
    attribute=value[2].text
    memory=value[3].text
    equip_slots=value[4].text
    hp=value[5].text
    sp=value[6].text
    atk=value[7].text
    dfc=value[8].text
    intt=value[9].text
    spd=value[10].text

    data={
        'no':no,
        'digimon':digimon,
        'image':image,
        'stage':stage,
        'type':tipe,
        'attribute':attribute,
        'memory':memory,
        'equip slots':equip_slots,
        'hp':hp,
        'sp':sp,
        'atk':atk,
        'def':dfc,
        'int':intt,
        'spd':spd
    }

    dataJSON.append(data)

# print(dataJSON)

import json
with open('digimon.json', 'w') as x:
    json.dump(dataJSON, x)