#!/usr/bin/python3
'''
@File : messagemodel.py

@Time : 2020/6/26

@Author : Boholder

@Function :

'''

import jellygolem.jg_emotion.emotionwheelprocess as emotionproc


class MsgModel:
    '''
    One message with corresponding emotion.
    '''

    def __init__(self, emotion: tuple = (0, 0),
                 msg: str = '...'):
        self.emotion_value = emotion
        self.emotion_label = emotionproc.find_closest_label(*emotion)
        self.message = msg


class MsgPairModel:
    '''
    Event message & reaction message combine in one model.
    '''

    def __init__(self, event_msgmodel: MsgModel = MsgModel(),
                 reaction_msgmodel: MsgModel = MsgModel()):
        self.event = event_msgmodel
        self.reaction = reaction_msgmodel
