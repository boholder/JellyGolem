#!/usr/bin/python3
'''
@File : emotionwheel.py

@Time : 2020/6/1

@Author : Boholder

@Function : Build a polar coordinate system for Robert Plutchik's 'Wheel of
            Emotions'.


'''

from enum import Enum
from math import pi, cos, pow


class EmotionCoordinate(Enum):
    '''
    Set polar coordinate system values for words(labels) in wheel.
    From top(the label "joy"), then clockwise.
    Add a new emotion called BROKEN, which radius=0.

    value: (radian[float] , radius[float])
    radius range: [0,1]
    '''

    BROKEN = (0, 0)
    ECSTASY = (pi * 0.5, 0.2)
    JOY = (pi * 0.5, 0.5)
    SERENITY = (pi * 0.5, 0.8)
    LOVE = (pi * 0.375, 0.5)
    ADMIRATION = (pi * 0.25, 0.2)
    TRUST = (pi * 0.25, 0.5)
    ACCEPTANCE = (pi * 0.25, 0.8)
    SUBMISSION = (pi * 0.125, 0.5)
    TERROR = (pi * 0.0, 0.2)
    FEAR = (pi * 0.0, 0.5)
    APPREHENSION = (pi * 0.0, 0.8)
    AWE = (pi * 1.875, 0.5)
    AMAZEMENT = (pi * 1.75, 0.2)
    SURPRISE = (pi * 1.75, 0.5)
    DISTRACTION = (pi * 1.75, 0.8)
    DISAPPROVAL = (pi * 1.625, 0.5)
    GRIEF = (pi * 1.5, 0.2)
    SADNESS = (pi * 1.5, 0.5)
    PENSIVENESS = (pi * 1.5, 0.8)
    REMORSE = (pi * 1.375, 0.5)
    LOATHING = (pi * 1.25, 0.2)
    DISGUST = (pi * 1.25, 0.5)
    BOREDOM = (pi * 1.25, 0.8)
    CONTEMPT = (pi * 1.125, 0.5)
    RAGE = (pi * 1.0, 0.2)
    ANGER = (pi * 1.0, 0.5)
    ANNOYANCE = (pi * 1.0, 0.8)
    AGGRESSIVENESS = (pi * 0.875, 0.5)
    VIGILANCE = (pi * 0.75, 0.2)
    ANTICIPATION = (pi * 0.75, 0.5)
    INTEREST = (pi * 0.75, 0.8)
    OPTIMISM = (pi * 0.625, 0.5)

    @staticmethod
    def find_closest_label(radian, radius):
        '''
        return a EmotionCoordinate member which closest with input.
        '''
        if radian == 0:
            return EmotionCoordinate.BROKEN

        result = None
        # init max value
        min_distance = 1

        for label in list(EmotionCoordinate):
            value = label.value
            distance = pow(radius, 2) + pow(value[1], 2) - \
                       2 * radius * value[1] * cos(radian - value[1])

            if distance < min_distance:
                min_distance = distance
                result = label

        return result
