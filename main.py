import requests
from bs4 import BeautifulSoup
import csv

links = {'1': "https://pk.altstu.ru/abitura/list/fakspc/55/",
         '2': 'https://pk.altstu.ru/abitura/list/fakspc/82/',
         '3': 'https://pk.altstu.ru/abitura/list/fakspc/83',
         '4': 'https://pk.altstu.ru/abitura/list/fakspc/85/#21111543',
         '5': 'https://pk.altstu.ru/abitura/list/fakspc/84/#21111543'
         }

for lk in links:
    url = links[lk]
    result = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('tr')
    budget = int(soup.find_all('em')[1].text)
    lbudget = int(soup.find_all('em')[2].text)
    cbudget = int(soup.find_all('em')[3].text)

    lb = 0
    cb = 0

    for line in table:
        if line.contents[3].text == 'да' and line.contents[4].text == "на общих основаниях":
            result.append(line)
        elif line.contents[3].text == 'да' and line.contents[4].text == "целевая квота":
            cb += 1
        elif line.contents[3].text == 'да' and line.contents[4].text == "льготная квота":
            lb += 1

    addSeets = (lbudget - lb) + (cbudget - cb)
    budget += addSeets
    n = 1
    htable = ['a', "b", 'c', 'd', "e"]

    with open(lk + '.csv', mode='w', encoding='utf-16', newline='') as f:

        wr = csv.writer(f)
        wr.writerow(['Budget:' + str(budget)])
        wr.writerow(htable)

        for words in result:
            ans = str(n), words.contents[1].text, words.contents[2].text, words.contents[5].text, words.contents[6].text
            n += 1
            wr.writerow(ans)

print("it's done")
put = input()
