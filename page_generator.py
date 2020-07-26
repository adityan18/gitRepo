import re
import json

filename = "template.html"
# id_text, name, gen, type_1, type_2, total, hp, attack, defence, sp_atk, sp_def, speed


type_color = json.load(open('types_color.json','r'))
def html_creator(id_text, name, gen, type_1, type_2, total, hp, attack, defence, sp_atk, sp_def, speed):

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

html_creator(1, 'Charmander', 1, 'fire', 'null', 10, 10, 10, 10, 10, 10, 10)
