#!/usr/bin/python3
'''
@File : emotionbtngroupwidget.py

@Time : 2020/6/8

@Author : Boholder

@Function : A widget displays 3*8 + 8 = 32 buttons,
            each button maps with an labeled emotion
            (in emotionwheelprocess.EmotionEnum , e.g. "joy" = (0.5*pi, 0.5))

'''

import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QApplication, QGroupBox,
                             QGridLayout, QPushButton, QButtonGroup, QLayout)

import jellygolem.configprocess as config
from jellygolem.jg_emotion.emotionwheelprocess import EmotionEnum


class EmotionButtonWidget(QPushButton):

    def __init__(self, emotion: EmotionEnum, *args,
                 **kwargs):
        super(EmotionButtonWidget, self).__init__(*args, **kwargs)
        self.emotion = emotion
        self.setText(config.LANG_CONFIG_PARSER['emotion words'][self.emotion.name])


class EmotionButtonGroupWidget(QGroupBox):
    emotion_signal = pyqtSignal(EmotionEnum)

    def __init__(self, *args,
                 **kwargs):
        super(EmotionButtonGroupWidget, self).__init__(*args, **kwargs)

        main_layout = QGridLayout()
        self.buttongroup = QButtonGroup()
        col = 0
        row = 0
        for name, member in EmotionEnum.__members__.items():

            # not make BLANK button, it causes error
            if name == 'BLANK':
                continue
            button = EmotionButtonWidget(member)
            button.clicked.connect(self.on_button_clicked)
            self.buttongroup.addButton(button, col)
            # 0,1,2
            # 3,
            # 4,5,6...
            if (col + 1) % 4 == 0:
                row += 1
                main_layout.addWidget(button, row, 0)
                row += 1
            else:
                main_layout.addWidget(button, row, col % 4)

            col += 1

        main_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        self.emotion_signal.emit(self.sender().emotion)


# if __name__ == '__main__':
#     app = QApplication([])
#     ex = EmotionButtonGroupWidget()
#     ex.show()
#     sys.exit(app.exec_())
