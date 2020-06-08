#!/usr/bin/python3
'''
@File : configprocess.py

@Time : 2020/6/5

@Author : Boholder

@Function : Process config files.

'''

import configparser
from ast import literal_eval

CONFIG_PATH = '../config/'
I18N_CONFIG_PATH = CONFIG_PATH + 'i18n/'
ROBOT_CONFIG_PATH = CONFIG_PATH + 'robot/'


def load_config(filename):
    parser = configparser.ConfigParser()
    parser.read(CONFIG_PATH + filename + '.ini')
    return parser


def load_i18n_config(langname):
    parser = configparser.ConfigParser()
    parser.read(I18N_CONFIG_PATH + langname + '.ini')
    return parser


def load_robot_config(robotname):
    parser = configparser.ConfigParser()
    parser.read(ROBOT_CONFIG_PATH + robotname + '/robot-config.ini')
    return parser


def type_convert(items):
    result = []
    for (key, value) in items:
        try:
            value = int(value)
            result.append((key, value))
            continue
        except ValueError:
            pass
        try:
            value = float(value)
            result.append((key, value))
            continue
        except ValueError:
            pass
        result.append((key, value))
    return result


def load_section_dict(configparser, partname):
    part = configparser[partname]
    return dict(type_convert(part.items()))


GENERAL = load_section_dict(load_config('general-config'), 'general')
ROBOT = load_section_dict(load_robot_config(GENERAL['robot']), 'robot')
LANG_CONFIG_PARSER = load_i18n_config(GENERAL['language'])
