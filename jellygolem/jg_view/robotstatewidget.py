#!/usr/bin/python3
'''
@File : robotstatewidget.py

@Time : 2020/6/9

@Author : Boholder

@Function : This widget display robot's current state,
            such as name, internal emotion, favorability.

'''

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QLayout)

import jellygolem.configprocess as config
import jellygolem.jg_emotion.emotionwheelprocess as emotionproc


class RobotStateWidget(QWidget):

    def __init__(self, name: str, favorability: int, emotion: tuple, *args, **kwargs):
        super(RobotStateWidget, self).__init__(*args, **kwargs)

        # init properties
        self.name = name
        self.favorability = favorability
        self.emotion = emotion

        # make labels
        name_label = QLabel(config.UI_CONFIG['robot-name'] + ': ')
        name_value_label = QLabel(self.name)

        favor_label = QLabel(config.UI_CONFIG['robot-favorability'] + ': ')
        favor_value_label = QLabel(str(self.favorability))

        emotionlab_label = QLabel(config.UI_CONFIG['robot-emotion-label'] + ': ')
        emotion_enum = emotionproc.find_closest_label(*self.emotion)
        emotionlab_value_label = QLabel(
            config.LANG_CONFIG_PARSER['emotion words'][emotion_enum.name])

        emotionval_label = QLabel(config.UI_CONFIG['robot-emotion-value'] + ': ')
        emotionval_value_label = QLabel(str(self.emotion))

        # add label into layout
        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(name_value_label, 0, 1)
        layout.addWidget(favor_label, 1, 0)
        layout.addWidget(favor_value_label, 1, 1)
        layout.addWidget(emotionlab_label, 2, 0)
        layout.addWidget(emotionlab_value_label, 2, 1)
        layout.addWidget(emotionval_label, 3, 0)
        layout.addWidget(emotionval_value_label, 3, 1)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    font = QFont()
    # font.setPixelSize(18)
    app.setFont(font)
    window = RobotStateWidget('tara', 20, (0, 0))
    window.show()
    sys.exit(app.exec_())
