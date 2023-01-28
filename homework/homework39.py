from random import choice
import json


def get_person():
    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel,

    }
    return person


def write_json(person_dict):
    ids = ''
    try:
        data = json.load(open('persons_dict.json'))
    except FileNotFoundError:
        data = {}

    while len(ids) != 9:
        ids += choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])

    data[ids] = person_dict
    with open('persons_dict.json', 'w') as f:
        json.dump(data, f, indent=4)


for i in range(5):
    write_json(get_person())
