import json
from bs4 import BeautifulSoup
import re
from time import sleep
import requests
import pandas as pd
from time import time

# from page_generator import html_creator as hc

start = time()
html = open('pokedex.html').read()

soup = BeautifulSoup(html, 'html.parser')


id_text = []
name = []
type_text = []
total = []
hp = []
attack = []
defence = []
sp_atk = []
sp_def = []
speed = []
gen = []
prev_name = []
next_name = []


def get_detail():
    tag = soup('td')
    i = 0
    for cell in tag:

        if(i % 10 == 0):

            id_x = cell.text
            if(id_x not in id_text):

                id_text.append(id_x)
                flag = False

                id_y = int(id_x)

                if(id_y <= 151):
                    gen.append(1)
                elif(id_y <= 251):
                    gen.append(2)
                elif(id_y <= 386):
                    gen.append(3)
                elif(id_y <= 492):
                    gen.append(4)
                elif(id_y <= 648):
                    gen.append(5)
                elif(id_y <= 720):
                    gen.append(6)
                elif(id_y <= 803):
                    gen.append(7)
                else:
                    gen.append(8)

                i += 1

            else:
                flag = True
                i += 1
                continue

        elif(i % 10 == 1 and flag == False):
            name_x = cell.find('a', attrs={'class': 'ent-name'})
            name_y = name_x.text
            name.append(name_y)
            print(name_y)
            image(name_y.lower())
            i += 1

        elif (i % 10 == 2 and flag == False):
            type_x = cell.text.split()
            if(len(type_x) == 1):
                type_x.append('Null')
            type_text.append(type_x)
            i += 1

        elif (i % 10 == 3 and flag == False):
            total_x = cell.text
            total.append(total_x)
            i += 1

        elif (i % 10 == 4 and flag == False):
            hp_x = cell.text
            hp.append(hp_x)
            i += 1

        elif (i % 10 == 5 and flag == False):
            attack_x = cell.text
            attack.append(attack_x)
            i += 1

        elif (i % 10 == 6 and flag == False):
            defence_x = cell.text
            defence.append(defence_x)
            i += 1

        elif (i % 10 == 7 and flag == False):
            spatk_x = cell.text
            sp_atk.append(spatk_x)
            i += 1

        elif (i % 10 == 8 and flag == False):
            spdef_x = cell.text
            sp_def.append(spdef_x)
            i += 1

        elif (i % 10 == 9 and flag == False):
            speed_x = cell.text
            speed.append(speed_x)
            i = 0

        else:
            if(i % 10 == 9):
                flag == True
                i = 0
                continue
            i += 1
    prev_next(name)


def prev_next(name_list):
    count = 0

    prev_name.append('Null')
    for i in name_list:
        prev_name.append(i)
        if (count == 0):
            count = 1
            continue
        next_name.append(i)
    prev_name.pop()
    next_name.append('Null')


def put_csv():
    df = pd.DataFrame({'ID': id_text, 'Pokemon': name, 'Generation': gen, 'Type': type_text,
                       'Total': total, 'HP': hp, 'Attack': attack, 'Defence': defence,
                       'Sp.Atack': sp_atk, 'Sp.Defence': sp_def, 'Speed': speed,
                       'Previous': prev_name, 'Next': next_name})
    df.to_csv('pokemon.csv', index=False, encoding='utf-8')

    print('CSV Done.....')


def image(name):

    url = 'https://img.pokemondb.net/artwork/' + name + '.jpg'
    response = requests.get(url)

    f_name = name + '.png'
    file = open('img/' + f_name, "wb")

    file.write(response.content)
    file.close()
    print(name + 'image added')


if __name__ == "__main__":
    get_detail()
    put_csv()

    end = time()
    print('Time:', end-start)
