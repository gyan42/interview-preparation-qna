

from numpy.random import choice

def generate_randon_char_steam(char_list, probabilit):
    while(1):
        c = choice(a=char_list, p=probabilit, size=1)[0]
        print(c, end=' ')

generate_randon_char_steam(char_list=['a', 'b', 'c'], probabilit=[0.3, 0.5, 0.2])
