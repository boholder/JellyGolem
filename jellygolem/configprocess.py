#!/usr/bin/python3
'''
@File : configprocess.py

@Time : 2020/6/5

@Author : Boholder

@Function : Process config files.

'''

import configparser
import os

_CONFIG_PATH = 'config/'
_I18N_CONFIG_PATH = _CONFIG_PATH + 'i18n/'
_ROBOT_CONFIG_PATH = 'robot/'


def load_config(filename):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__),
                             _CONFIG_PATH) + filename + '.ini')
    return parser


def load_i18n_config(langname):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__),
                             _I18N_CONFIG_PATH) + langname + '.ini')
    return parser


def load_robot_config(robotname):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__),
                             _ROBOT_CONFIG_PATH) + robotname + '/robot-config.ini')
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


def load_section_dict(parser, partname):
    part = parser[partname]
    return dict(type_convert(part.items()))


GENERAL_DICT = load_section_dict(load_config('general-config'), 'general')
ROBOT_DICT = load_section_dict(load_robot_config(GENERAL_DICT['robot']), 'robot')
LANG_CONFIG_PARSER = load_i18n_config(GENERAL_DICT['language'])

ROBOT_PKG_PATH = os.path.join(os.path.dirname(__file__),
                              _ROBOT_CONFIG_PATH) + GENERAL_DICT['robot']

UI_CONFIG = dict(LANG_CONFIG_PARSER['ui'])