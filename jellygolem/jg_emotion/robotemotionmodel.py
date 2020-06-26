#!/usr/bin/python3
'''
@File : robotemotionmodel.py

@Time : 2020/6/5

@Author : Boholder

@Function : Process emotion, change robot's emotion, output robot's display emotion.
                            +--------------------------+
            +-------------+ | inner emotion memory     |
            |event emotion| |   +-------------------+  |
            +----+------------->+ change inner emotion |
                 |          |   | for next loop     |  |
                 |          |   |                   |  |
                 |          |   +-------------------+  |
                 |          |                          |
                 |          |    output current  ------------^--------------+
                 |          |    emotion state         |     |              |   +-----------------+
                 |          +--------------------------+     |  combine two +-->+displayed emotion|
                 |                                           |   emotions   |   +-----------------+
                 +------------------------------------------>+--------------+


'''

import datetime
from math import pow, log, ceil

import jellygolem.jg_emotion.emotionwheelprocess as wheel


class RobotEmotionData:

    def __init__(self, emotion: tuple = (0, 0), favorability: int = 0,
                 iescale: float = 1, rescale: float = 0.5):
        self.emotion = emotion
        self.favorability = favorability
        # Internal-External Scale (I-E Scale)
        # http://carter.psych.upenn.edu/dmidi/Internal-External_Scale.html
        # This will modulate the weight of external events affect on the emotion of the robot.
        # value : 0 ~ 1, 0 not include,
        # The higher the number, the more easily influenced the robot.
        self.iescale = iescale

        # Rational-Emotional scale
        # This will determine the share of immediate versus internal emotions
        # in the robot's directly displayed emotions in response to events.
        # value : 0 ~ 1, 0 not include,
        # The higher the value,
        # the closer the displayed emotion is to the input event emotion.
        self.rescale = rescale


class RobotEmotionModel:
    '''
    store & process emotion variable.
    '''

    def __init__(self, initdata: RobotEmotionData = RobotEmotionData()):
        '''
        emotion: emotion tuple
        '''

        # this is the internal emotion value
        self.emotion = initdata.emotion
        self.favorability = initdata.favorability
        self.iescale = initdata.iescale
        self.rescale = initdata.rescale

        # mark a time for emotional fading mechanisms
        self._start_time = datetime.datetime.utcnow()

    def emotion_decrease(self):
        '''
        The intensity of emotion decreases over time.
        The formula is taken from Hermann Ebbinghaus's forgetting curve.
        http://psychclassics.yorku.ca/Ebbinghaus/memory7.htm
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4492928/
        '''

        # t: the time in minutes counting from last emotion change.
        new_timestamp = datetime.datetime.utcnow()
        t = (new_timestamp - self._start_time).total_seconds() / 60
        # speed up response, when time interval is less than 1 minute.
        if t < 1:
            pass
        else:
            # record new timestamp
            self._start_time = new_timestamp
            # calculate new emotion tuple
            decreased = self.emotion[1] * 1.84 / (1.84 + pow(log(t, 10), 1.25))
            self.emotion = (self.emotion[0], decreased)

    def receive_emotion(self, in_emotion: tuple):
        '''
        Why bother design another emotion-react-emotion mapping,
        just label an emotion with the human's expect response about it.

        Return displayed emotion tuple.
        '''

        if wheel.is_negative_emotion(in_emotion):
            # favorability reduce the impact of negative events on robot's emotions
            # full favorability(=500) will reduce 50% impact
            reduced = in_emotion[1] * (1 - self.favorability / 1000)
            in_emotion = (in_emotion[0], reduced)

            # emotion changes favorability,
            # if emotion radius bigger than 0.7, +-2,or +-1
            self.favorability -= ceil(reduced / 0.7)
        else:
            self.favorability += ceil(in_emotion[1] / 0.7)

        # emotion intensity decrease
        self.emotion_decrease()
        old_emotion = self.emotion

        # change internal emotion
        self.emotion = wheel.calc_muti_emotions_mean(
            [(in_emotion[0], in_emotion[1] * self.iescale), old_emotion])

        # displayed emotion = mean(immediate emotion * r-e-scale, internal emotion)
        return wheel.calc_muti_emotions_mean(
            [(in_emotion[0], in_emotion[1] * self.rescale),
             old_emotion])
