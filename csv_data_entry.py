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

# def json_type_creation():
#     json_tag = soup('option')
#     type_json = {}
#     count = 0
#     for i in json_tag:
#         if(i.text == '- All -'):
#             type_json_ = 'Null'
#         else:
#             type_json_ = i.text

#         type_json[type_json_] = count
#         count += 1

#     with open('types.json', 'w')as outfile:
#         json.dump(type_json, outfile, indent=4)

#     print('types.json created')


# json_type_creation()

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


def put_csv():
    df = pd.DataFrame({'ID': id_text, 'Pokemon': name, 'Generation': gen, 'Type': type_text,
                       'Total': total, 'HP': hp, 'Attack': attack, 'Defence': defence,
                       'Sp.Atack': sp_atk, 'Sp.Defence': sp_def, 'Speed': speed})
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


# def type_table():
#     type_json = json.load(open('types.json'))
#     print('\nAdding Types\n')
#     for element in type_json:
#         cur.execute('''INSERT OR IGNORE INTO Type1 (ID, Type)
#             VALUES ( ?, ?)''', (type_json[element], element))
#         cur.execute('''INSERT OR IGNORE INTO Type2 (ID, Type)
#             VALUES ( ?, ?)''', (type_json[element], element))
#         print(element, 'Added')
#     conn.commit()

#     print('\nType Table Completed.....\n')

#     getting_detials(type_json)


# def getting_detials(type_json):
#     for i in range(len(tag)):

#         tag_ = str(tag[i])


#     pokemon_table_entry()


# def pokemon_table_entry():
#     for i in range(len(name)):

#         cur.execute('''INSERT OR IGNORE INTO Pokemon (ID, Name, Generation,Type_1, Type_2, Total, Hp, Attack, Defence, Sp_Attack, Sp_Defence, Speed)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                     (id_text[i], name[i], gen[i], type_int[i][0], type_int[i][1], total[i], hp[i], attack[i], defence[i], sp_atk[i], sp_def[i], speed[i]))
#         print(id_text[i], name[i], 'Added')

#         image(name[i].lower())

#         hc(id_text[i], name[i], gen[i], type_int[i][0], type_int[i][1], total[i], hp[i], attack[i], defence[i], sp_atk[i], sp_def[i], speed[i])

#     conn.commit()

# #CALL DIRECTLY OR USE SELECT


# if __name__ == "__main__":
#     table_create()
#     json_type_creation()
#     type_table()
