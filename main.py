#!/usr/bin/python

import subprocess
import re
import sys
from pymatrix import matrix

def get_slop():
    rect_str = subprocess.check_output(['slop']).decode("utf-8")
    rgxp = re.search('([0-9]+)x([0-9]+)\+([0-9]+)\+([0-9]+)', rect_str)
    return {'w' : int(rgxp.groups()[0]),
            'h' : int(rgxp.groups()[1]),
            'x' : int(rgxp.groups()[2]),
            'y' : int(rgxp.groups()[3])}

def scale(sx, sy):
    return matrix([[sx, 0, 0], \
                   [0, sy, 0], \
                   [0,  0, 1]])

def translate(x, y):
    return matrix([[1, 0, x], \
                   [0, 1, y], \
                   [0, 0, 1]])

def get_xinput_id(name):
    lines = subprocess.check_output(['xinput', '--list']).decode('utf-8')

    keyboard = False
    pointer = False

    for line in lines.split('\n'):
        if 'Virtual core pointer' in line:
            pointer = True
        elif 'Virtual core keyboard' in line:
            keyboard = True

        if name in line and pointer:
            search = re.search('^.*id=([0-9]+).*$', line)
            return search.groups()[0]
    return None

def get_screen_dimensions():
    lines = subprocess.check_output(['xrandr']).decode('utf-8')
    line = lines.split('\n')[0]
    search = re.search('^.*current ([0-9]+) x ([0-9]+).*$', line)
    return {'width': int(search.groups()[0]),
            'height': int(search.groups()[1])}

def matrix_args(transform):
    return list(map(lambda x: str(x[2]), transform))

def set_xinput_transform_matrix(xinput_id, transform):
    subprocess.check_output(['xinput', '--set-prop', xinput_id, '--type=float',\
                             'Coordinate Transformation Matrix'] + \
                            matrix_args(transform))

def main(argv):
    slop = get_slop()
    screen_dim = get_screen_dimensions()

    tr = translate(slop['x']/screen_dim['width'], slop['y']/screen_dim['height'])
    sc1 = scale(slop['w']/screen_dim['width'], slop['h']/screen_dim['height'])
    transform = tr * sc1

    xinput_id = get_xinput_id(argv[1])

    if not xinput_id:
        print("Device", argv[1], "not found!")
    else:
        set_xinput_transform_matrix(xinput_id, transform)
        print("Success!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("This program takes a single argument with your tablet name!")
    else:
        if sys.argv[1] == "Ribbit":
            print("Wibbit")
        else:
            main(sys.argv)
