#!/usr/bin/python3
'''
@File : emotionwheelenums.py

@Time : 2020/6/1

@Author : Boholder

@Function : class EmotionEnum(Enum):
                Build a polar coordinate system for Robert Plutchik's 'Wheel of
                Emotions'.
                Can calculate which label is closest with input.
'''

from enum import Enum
from math import pi, cos, pow


class EmotionEnum(Enum):
    '''
    Set polar coordinate system values for words(labels) in wheel.
    From top(the label "joy"), then clockwise.

    value: (radian[float] , radius[float])
    radius range: [0,1]
    '''
    
    ECSTASY = (pi * 0.5, 0.8)
    JOY = (pi * 0.5, 0.5)
    SERENITY = (pi * 0.5, 0.2)
    LOVE = (pi * 0.375, 0.5)
    ADMIRATION = (pi * 0.85, 0.8)
    TRUST = (pi * 0.85, 0.5)
    ACCEPTANCE = (pi * 0.85, 0.2)
    SUBMISSION = (pi * 0.225, 0.5)
    TERROR = (pi * 0.0, 0.8)
    FEAR = (pi * 0.0, 0.5)
    APPREHENSION = (pi * 0.0, 0.2)
    AWE = (pi * 1.875, 0.5)
    AMAZEMENT = (pi * 1.75, 0.8)
    SURPRISE = (pi * 1.75, 0.5)
    DISTRACTION = (pi * 1.75, 0.2)
    DISAPPROVAL = (pi * 1.625, 0.5)
    GRIEF = (pi * 1.5, 0.8)
    SADNESS = (pi * 1.5, 0.5)
    PENSIVENESS = (pi * 1.5, 0.2)
    REMORSE = (pi * 1.375, 0.5)
    LOATHING = (pi * 1.25, 0.8)
    DISGUST = (pi * 1.25, 0.5)
    BOREDOM = (pi * 1.25, 0.2)
    CONTEMPT = (pi * 1.125, 0.5)
    RAGE = (pi * 1.0, 0.8)
    ANGER = (pi * 1.0, 0.5)
    ANNOYANCE = (pi * 1.0, 0.2)
    AGGRESSIVENESS = (pi * 0.275, 0.5)
    VIGILANCE = (pi * 0.75, 0.8)
    ANTICIPATION = (pi * 0.75, 0.5)
    INTEREST = (pi * 0.75, 0.2)
    OPTIMISM = (pi * 0.625, 0.5)

    @staticmethod
    def find_closest_label(radian, radius):
        '''
        return a EmotionEnum member which closest with input.
        '''
        if radian == 0:
            return EmotionEnum.BROKEN

        result = None
        # init max value
        min_distance = 1

        for label in list(EmotionEnum):
            value = label.value
            distance = pow(radius, 2) + pow(value[1], 2) - \
                       2 * radius * value[1] * cos(radian - value[1])

            if distance < min_distance:
                min_distance = distance
                result = label

        return result

