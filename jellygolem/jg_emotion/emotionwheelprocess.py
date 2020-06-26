#!/usr/bin/python3
'''
@File : emotionwheelprocess.py

@Time : 2020/6/1

@Author : Boholder

@Function : class EmotionEnum(Enum):
                Build a polar coordinate system for Robert Plutchik's 'Wheel of
                Emotions'.
            Calculate which label is closest with input.
'''

from enum import Enum
from math import pi, cos, sin, atan2, sqrt


class EmotionEnum(Enum):
    '''
    Set polar coordinate system values for words(labels) in wheel.
    From top(the label "joy"), then clockwise.

    value: (radian[float] , radius[float])
    radius range: [0,1)
    '''

    BLANK = (0, 0)
    ECSTASY = (pi * 0.5, 0.8)
    JOY = (pi * 0.5, 0.5)
    SERENITY = (pi * 0.5, 0.2)
    LOVE = (pi * 0.375, 0.5)
    ADMIRATION = (pi * 0.25, 0.8)
    TRUST = (pi * 0.25, 0.5)
    ACCEPTANCE = (pi * 0.25, 0.2)
    SUBMISSION = (pi * 0.125, 0.5)
    TERROR = (pi * 0.0, 0.8)
    FEAR = (pi * 0.0, 0.5)
    APPREHENSION = (pi * 0.0, 0.2)
    AWE = (pi * -0.125, 0.5)
    AMAZEMENT = (pi * -0.25, 0.8)
    SURPRISE = (pi * -0.25, 0.5)
    DISTRACTION = (pi * -0.25, 0.2)
    DISAPPROVAL = (pi * -0.375, 0.5)
    GRIEF = (pi * -0.5, 0.8)
    SADNESS = (pi * -0.5, 0.5)
    PENSIVENESS = (pi * -0.5, 0.2)
    REMORSE = (pi * -0.625, 0.5)
    LOATHING = (pi * -0.75, 0.8)
    DISGUST = (pi * -0.75, 0.5)
    BOREDOM = (pi * -0.75, 0.2)
    CONTEMPT = (pi * -0.875, 0.5)
    RAGE = (pi * 1.0, 0.8)
    ANGER = (pi * 1.0, 0.5)
    ANNOYANCE = (pi * 1.0, 0.2)
    AGGRESSIVENESS = (pi * 0.875, 0.5)
    VIGILANCE = (pi * 0.75, 0.8)
    ANTICIPATION = (pi * 0.75, 0.5)
    INTEREST = (pi * 0.75, 0.2)
    OPTIMISM = (pi * 0.625, 0.5)


def find_closest_label(radian: float, radius: float):
    '''
    return a EmotionEnum member which closest with input.
    '''

    check_radius(radius)

    if radian == 0 and radius == 0:
        return EmotionEnum.BLANK

    result = None
    # init max value
    min_distance = 1

    for label in list(EmotionEnum):
        value = label.value
        distance = radius ** 2 + value[1] ** 2 \
                   - 2 * radius * value[1] * cos(radian - value[0])

        if distance < min_distance:
            min_distance = distance
            result = label

    return result


def calc_muti_emotions_mean(emotionlist: list):
    '''
    Calculate the mean emotion of multiple given emotions.
    Return an emotion tuple.
    '''

    x = 0
    y = 0
    for (radian, radius) in emotionlist:
        check_radius(radius)
        x += radius * cos(radian)
        y += radius * sin(radian)

    x /= len(emotionlist)
    y /= len(emotionlist)

    try:
        meanradius = round(sqrt(x ** 2 + y ** 2), 6)
        # the atan2() automatically deal with problems such as 'y=0'
        meanradian = round(atan2(y, x), 6)
        check_radius(meanradius)
        return meanradian, meanradius
    except ZeroDivisionError:
        return meanradian, 0.0
    except ValueError:
        return meanradian, 1.0


def check_radius(radius: float):
    '''
    Check if radius not more than 1.
    '''
    if radius > 1:
        raise ValueError('Radius more than 1: {}'.format(radius))


def is_negative_emotion(emotion: tuple):
    '''
    This is a negative emotion,
    if the radian not close to anticipation, joy or trust.
    '''
    if emotion[0] < 0.125 * pi or emotion[0] > 0.75 * pi:
        return True
    else:
        return False


def calc_paint_position(radian: float, radius: float):
    '''
    Calculate current emotion's position on /resource/emotion-wheel.png
    Wheel picture size: 650*650
    Heart picture size: 16*16
    '''

    # On wheel in picture, more smaller the radius, more stronger the emotion.
    # But in EmotionEnum, bigger value means stronger emotion.
    # So we just flip radius value to suit the picture.
    radius = 1.0 - radius

    # Picture parts' widths are not equal
    if radius > 0.35:
        length = (radius - 0.35) * 210.0 + 125.0
    else:
        length = radius * 357.0

    # 325-8=317 pix for wheel.png center is (325,325), heart.png size is 16*16
    return 317.0 + length * cos(radian), 317.0 - length * sin(radian)
