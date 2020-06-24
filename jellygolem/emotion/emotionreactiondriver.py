#!/usr/bin/python3
'''
@File : emotionreactiondriver.py

@Time : 2020/6/24

@Author : Boholder

@Function : A driver for simulating event happening & robot's reaction.
            Will be replaced by event system.

'''

import jellygolem.configprocess as config
from jellygolem.emotion.emotionwheelprocess import EmotionEnum


def get_event_by_emotion(emotion: EmotionEnum):
    return config.LANG_CONFIG_PARSER['emotion trigger events'][emotion.name]


def get_reaction_by_emotion(emotion: EmotionEnum):
    return config.LANG_CONFIG_PARSER['emotion reaction words'][emotion.name]
