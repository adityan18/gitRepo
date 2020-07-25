import sqlite3
import json
from bs4 import BeautifulSoup
import re
from time import sleep
import requests


conn = sqlite3.connect('Pokemon DB.sqlite')
cur = conn.cursor()

html = open('pokedex.html').read()

soup = BeautifulSoup(html, 'html.parser')


tag = soup('td')

name = []
id_text = []
type_int = []
total = []
hp = []
attack = []
defence = []
sp_atk = []
sp_def = []
speed = []
gen = []


def table_create():
    print('Creating Tables...')
    cur.executescript('''
    DROP TABLE IF EXISTS Type1;
    DROP TABLE IF EXISTS Type2;
    DROP TABLE IF EXISTS Pokemon;

        CREATE TABLE IF NOT EXISTS Pokemon (
            ID  INTEGER NOT NULL PRIMARY KEY UNIQUE,
            Name TEXT UNIQUE,
            Generation INTEGER,
            Type_1 INTEGER,
            Type_2 INTEGER,
            Total INTEGER,
            HP INTEGER,
            Attack INTEGER,
            Defence INTEGER,
            Sp_Attack INTEGER,
            Sp_Defence INTEGER,
            Speed INTEGER
            );

        CREATE TABLE IF NOT EXISTS Type1 (
            ID INTEGER ,
            Type TEXT
        );

        CREATE TABLE IF NOT EXISTS Type2 (
            ID INTEGER ,
            Type TEXT
        )

    ''')
    print('\nTables Created\n')


def json_type_creation():
    json_tag = soup('option')
    type_json = {}
    count = 0
    for i in json_tag:
        try:
            type_json_ = re.findall('"(.+)"', str(i))[0]
        except:
            type_json_ = 'null'
        type_json[type_json_] = count
        count += 1

    with open('types.json', 'w')as outfile:
        json.dump(type_json, outfile, indent=4)


def type_table():
    type_json = json.load(open('types.json'))
    print('\nAdding Types\n')
    for element in type_json:
        cur.execute('''INSERT OR IGNORE INTO Type1 (ID, Type)
            VALUES ( ?, ?)''', (type_json[element], element))
        cur.execute('''INSERT OR IGNORE INTO Type2 (ID, Type)
            VALUES ( ?, ?)''', (type_json[element], element))
        print(element, 'Added')
    conn.commit()

    print('\nType Table Completed.....\n')

    getting_detials(type_json)


def getting_detials(type_json):
    for i in range(len(tag)):

        tag_ = str(tag[i])

        if(i % 10 == 0):
            continue

        elif(i % 10 == 1):
            id_ = re.findall('#(.\S+)', tag_)[0]
            if(id_ not in id_text):
                id_text.append(id_)
                flag = False
                id_ = int(id_)
                if(id_ <= 151):
                    gen.append(1)
                elif(id_ <= 251):
                    gen.append(2)
                elif(id_ <= 386):
                    gen.append(3)
                elif(id_ <= 492):
                    gen.append(4)
                elif(id_ <= 648):
                    gen.append(5)
                elif(id_ <= 720):
                    gen.append(6)
                elif(id_ <= 803):
                    gen.append(7)
                else:
                    gen.append(8)

            else:
                flag = True
                continue

            try:
                name.append(re.findall('">(\S+)</a>', tag_)[0])
            except:
                if('Mr. Mime' in tag_):
                    name.append('Mr. Mime')
                elif('Mr. Rime' in tag_):
                    name.append('Mr. Rime')

        elif (i % 10 == 2 and flag == False):
            type_text = (re.findall('">(\S+)</a>', tag_))  # list
            type_int_ = []
            for ele in type_text:
                type_int_.append(type_json[ele.lower()])

            if(len(type_int_) == 1):
                type_int_.append(0)
            type_int.append(type_int_)

        elif (i % 10 == 3 and flag == False):
            total.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 4 and flag == False):
            hp.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 5 and flag == False):
            attack.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 6 and flag == False):
            defence.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 7 and flag == False):
            sp_atk.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 8 and flag == False):
            sp_def.append(re.findall('">(\S+)</td>', tag_)[0])

        elif (i % 10 == 9 and flag == False):
            speed.append(re.findall('">(\S+)</td>', tag_)[0])

    pokemon_table_entry()


def pokemon_table_entry():
    for i in range(len(name)):

        cur.execute('''INSERT OR IGNORE INTO Pokemon (ID, Name, Generation,Type_1, Type_2, Total, Hp, Attack, Defence, Sp_Attack, Sp_Defence, Speed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (id_text[i], name[i], gen[i], type_int[i][0], type_int[i][1], total[i], hp[i], attack[i], defence[i], sp_atk[i], sp_def[i], speed[i]))
        print(id_text[i], name[i], 'Added')

        image(name[i].lower())

    conn.commit()


def image(name):

    url = 'https://img.pokemondb.net/artwork/' + name + '.jpg'
    response = requests.get(url)

    f_name = name + '.png'
    file = open('img/' + f_name, "wb")
    
    file.write(response.content)

    file.close()


if __name__ == "__main__":
    table_create()
    json_type_creation()
