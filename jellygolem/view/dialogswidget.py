#!/usr/bin/python3
'''
@File : dialogswidget.py

@Time : 2020/6/9

@Author : Boholder

@Function : This widget shows user (emotion label) input
                & robot's response (in emotion description).

'''

import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QFrame, QLayout,
                             QVBoxLayout, QHBoxLayout)

import jellygolem.configprocess as config
from jellygolem.emotion.emotionwheelprocess import EmotionEnum
import jellygolem.emotion.emotionreactiondriver as driver


class DialogsWidget(QWidget):

    def __init__(self, event_emotion: EmotionEnum, event_info: str, react_emotion: EmotionEnum,
                 react_info: str, *args, **kwargs):
        super(DialogsWidget, self).__init__(*args, **kwargs)

        # init properties
        self.event_emotion = event_emotion
        self.event_info = event_info
        self.react_emotion = react_emotion
        self.react_info = react_info

        # make widgets
        input_emotion_label = QLabel(config.UI_CONFIG['input-emotion-label'] + ': ')
        output_emotion_label = QLabel(config.UI_CONFIG['output-emotion-label'] + ': ')
        description_label1 = QLabel(config.UI_CONFIG['description'] + ': ')
        description_label2 = QLabel(config.UI_CONFIG['description'] + ': ')

        input_emotion_value_label = QLabel(
            config.LANG_CONFIG_PARSER['emotion words'][self.event_emotion.name])
        input_emotion_value_label.setFrameShape(QFrame.Box)

        output_emotion_value_label = QLabel(
            config.LANG_CONFIG_PARSER['emotion words'][self.react_emotion.name])
        output_emotion_value_label.setFrameShape(QFrame.Box)

        input_description = QLabel(self.event_info)
        input_description.setFrameShape(QFrame.Box)
        output_description = QLabel('"' + self.react_info + '"')
        output_description.setFrameStyle(QFrame.Box)

        layout = QGridLayout()
        layout.addWidget(input_emotion_label, 0, 0)
        layout.addWidget(input_emotion_value_label, 0, 1)
        layout.addWidget(description_label1, 0, 2)
        layout.addWidget(input_description, 0, 3)
        layout.addWidget(output_emotion_label, 1, 0)
        layout.addWidget(output_emotion_value_label, 1, 1)
        layout.addWidget(description_label2, 1, 2)
        layout.addWidget(output_description, 1, 3)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    font = QFont()
    # font.setPixelSize(18)
    app.setFont(font)
    window = DialogsWidget(EmotionEnum.JOY, driver.get_event_by_emotion(EmotionEnum.JOY),
                           EmotionEnum.JOY, driver.get_reaction_by_emotion(EmotionEnum.JOY))
    window.show()
    sys.exit(app.exec_())
