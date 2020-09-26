#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------------
# Name:        json_tools.py
# Purpose:
#
# Author:      Filipe Silva (filipeluizsilva@gmail.com)
#
# Created:     26/09/2020
# Copyright:   (c) Filipe Silva 2020
# Licence:     MIT
# -------------------------------------------------------------------------------

import json


def write_json(dct, json_file):
    """
    Write a json file.

    Args:
        dct (dict): the name of the dictionary that will be written in 
        json file.
        json_file (str): the name of json file. Must be 'name.json'.
    """
    with open(json_file, 'w', encoding='utf8') as file:
        json.dump(dct, file, ensure_ascii=False, sort_keys=True,
                  indent=4, separators=(',', ':'))


def read_json(json_file):
    """
    Read a json file.

    Args:
        json_file (str): name of the json file. Must be 'name.json'.

    Returns:
        dict: returns a dict of the json file.
    """
    with open(json_file, 'r', encoding='utf8') as file:
        return json.load(file)


if __name__ == '__main__':
    name = input('Name: ')
    age = input('Age: ')
    test = {'name': name, 'age': age}
    write_json(test, 'test.json')
    print(read_json('test.json'))
