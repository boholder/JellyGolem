#!/usr/bin/python3
'''
@File : abslanguage.py

@Time : 2020/6/2

@Author : Boholder

@Function : Abstract enum Classes for i18n modules.
            works like mixin class.

'''

from enum import Enum
from jellygolem.model.emotionwheel import EmotionCoordinate


class AbsEmotionWord(Enum):
    '''
    Labels in Robert Plutchik's 'Wheel of Emotions'.
    '''

    @staticmethod
    def translate_coordinate_to_word(sub, member):
        '''
        return the string value of same name member in EmotionCoordinate.
        '''
        return sub[member.name].value
