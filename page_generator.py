import re
import json
import re
import pandas as pd
from time import time
start = time()

pokemon_data = pd.read_csv('pokemon.csv', index_col='ID')
type_color = json.load(open('types_color.json','r'))


def html_creator(name, gen, type_text, total, hp, attack, defence, sp_atk, sp_def, speed):

    type_1 = type_text[0]
    type_2 = type_text[1]
    filename = "template.html"
    with open(filename, 'r+') as f:

        text = f.read()
        text = re.sub('NAME_L', name.lower(), text)
        text = re.sub('NAME', name, text)

        text = re.sub('GEN', 'Gen'+ str(gen), text)
        text = re.sub('TYPE1_L', type_1.lower(), text)
        text = re.sub('TYPE1', type_1, text)

        if(type_2 == 'null'):
            text = re.sub('<li class="TYPE2_L">TYPE2</li>', '', text)
        else:
            text = re.sub('TYPE2_L', type_2.lower(), text)
            text = re.sub('TYPE2', type_2, text)

        text = re.sub('COLOR', type_color[type_1], text)

        text = re.sub('TOTAL', str(total), text)
        text = re.sub('hp', str(hp), text)
        text = re.sub('ATTACK', str(attack), text)
        text = re.sub('DEFENCE', str(defence), text)
        text = re.sub('SPATK', str(sp_atk), text)
        text = re.sub('SPDEF', str(sp_def), text)
        text = re.sub('SPEED', str(speed), text)


        new_file = open('Gen' + str(gen) + '/' + name + '.html', 'w+')

        new_file.seek(0)

        new_file.write(text)

        new_file.truncate()
        print('HTML Created')


for i in range(len(pokemon_data)):
    row = pokemon_data.loc[i+1]
    name = row[0]
    gen = row[1]
    type_text = re.findall("'(\S+)'",row[2])
    total = row[3]
    hp = row[4]
    attack = row[5]
    defence = row[6]
    sp_atk = row[7]
    sp_def = row[8]
    speed = row[9]
    prev_name = row[10]
    next_name = row[11]
    
    html_creator(name, gen, type_text, total, hp, attack, defence, sp_atk, sp_def, speed)
    break



stop = time()
print('Time:', stop-start)
