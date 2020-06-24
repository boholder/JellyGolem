#!/usr/bin/python3
'''
@File : robotemotionmodel.py

@Time : 2020/6/5

@Author : Boholder

@Function : Process emotion, change robot's emotion, output robot's display emotion.
                            +--------------------------+
            +----------+    | inner emotion memory     |
            |  emotion   ++   |   +-------------------+  |
            +----+------------->+ change inner emotion |
                 |          |   | for next loop     |  |
                 |          |   |                   |  |
                 |          |   +-------------------+  |
                 |          |                          |
                 |          |    output current  ------------^--------------+
                 |          |    emotion state         |     |              |   +-----------------+
                 |          +--------------------------+     |   combind    +-->+displayed emotion|
                 |                                           |   emotions   |   +-----------------+
                 +------------------------------------------>+--------------+


'''

import datetime
from math import pow, log, ceil

import jellygolem.configprocess as config
import jellygolem.emotion.emotionwheelprocess as wheel


class EmotionProcessor:
    '''
    store & process emotion variable.
    '''

    def __init__(self, emotion=(0, 0), favorability=0, iescale=0.5, rescale=0.5):
        '''
        emotion: emotion tuple
        '''

        self.emotion = emotion
        self.favorability = favorability
        self.iescale = iescale
        self.rescale = rescale

        # mark a time for emotional fading mechanisms
        self._start_time = datetime.datetime.utcnow()

    @property
    def emotion(self):
        return self._emotion

    @property
    def favorability(self):
        return self._favorability

    @emotion.setter
    def emotion(self, emotion: tuple):
        '''
        This method is only for debugging.
        '''
        wheel.check_radius(emotion[1])
        self._emotion = emotion

    @favorability.setter
    def favorability(self, favorability: int):
        '''
        This method is only for debugging.
        '''
        self._favorability = favorability

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
        # record new timestamp
        self._start_time = new_timestamp
        # calculate new emotion tuple
        t = 60
        decreased = self.emotion[1] * 1.84 / (1.84 + pow(log(t, 10), 1.25))
        self.emotion = (self.emotion[0], decreased)

    def receive_emotion(self, emotion: tuple):
        '''
        Why bother design another emotion-react-emotion mapping,
        just label an emotion with the human's expect response about it.

        Return displayed emotion tuple.
        '''

        # favorability reduce the impact of negative events on robot's emotions
        # full favorability(=500) will reduce 50% impact
        if wheel.is_negative_emotion(emotion):
            reduced = emotion[1] * (1 - self.favorability / 1000)
            emotion = (emotion[0], reduced)

            # emotion changes favorability
            self.favorability -= ceil(reduced / 0.7)
        else:
            self.favorability += ceil(emotion[1] / 0.7)

        # emotion intensity decrease
        self.emotion_decrease()
        old_emotion = self.emotion

        # emotion change inner emotion
        self.emotion = wheel.clac_muti_emotions_mean([emotion * self.iescale, old_emotion])

        # displayed emotion = immediate emotion+ internal emotion
        return wheel.clac_muti_emotions_mean(
            [emotion * self.rescale, old_emotion * (1 - self.rescale)])


EmotionProcessor = EmotionProcessor((0.5 * 3.14, 1), config.ROBOT_DICT['favorability'],
                                    config.ROBOT_DICT['i-e-scale'], config.ROBOT_DICT['r-e-scale'])
