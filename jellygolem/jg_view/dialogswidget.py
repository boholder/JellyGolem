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
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QGridLayout, QFrame, QLayout)

import jellygolem.configprocess as config
from jellygolem.jg_conversation.messagemodel import MsgPairModel


class DialogsWidget(QWidget):

    def __init__(self, msgpair: MsgPairModel = MsgPairModel(), *args, **kwargs):
        super(DialogsWidget, self).__init__(*args, **kwargs)

        # init variable
        self.msgpair = msgpair
        self.event = self.msgpair.event
        self.reaction = self.msgpair.reaction

        # make widgets
        input_emotion_label = QLabel(config.UI_CONFIG['event-emotion'] + ': ')
        output_emotion_label = QLabel(config.UI_CONFIG['reaction-emotion'] + ': ')
        description_label1 = QLabel(config.UI_CONFIG['description'] + ': ')
        description_label2 = QLabel(config.UI_CONFIG['description'] + ': ')

        self.input_emotion_name_label = QLabel(
            config.LANG_CONFIG_PARSER['emotion words'][
                self.msgpair.event.emotion_label.name])
        self.input_emotion_name_label.setFrameShape(QFrame.Box)
        self.input_emotion_value_label = QLabel(str(self.event.emotion_value))
        self.input_emotion_value_label.setFrameShape(QFrame.Box)

        self.output_emotion_name_label = QLabel(
            config.LANG_CONFIG_PARSER['emotion words'][
                self.reaction.emotion_label.name])
        self.output_emotion_name_label.setFrameShape(QFrame.Box)
        self.output_emotion_value_label = QLabel(str(self.reaction.emotion_value))
        self.output_emotion_value_label.setFrameShape(QFrame.Box)

        self.input_description = QLabel(self.event.message)
        self.input_description.setFrameShape(QFrame.Box)
        self.output_description = QLabel('"' + self.reaction.message + '"')
        self.output_description.setFrameShape(QFrame.Box)

        layout = QGridLayout()
        layout.addWidget(input_emotion_label, 0, 0)
        layout.addWidget(self.input_emotion_name_label, 0, 1)
        layout.addWidget(self.input_emotion_value_label, 0, 2)
        layout.addWidget(description_label1, 0, 3)
        layout.addWidget(self.input_description, 0, 4)
        layout.addWidget(output_emotion_label, 1, 0)
        layout.addWidget(self.output_emotion_name_label, 1, 1)
        layout.addWidget(self.output_emotion_value_label, 1, 2)
        layout.addWidget(description_label2, 1, 3)
        layout.addWidget(self.output_description, 1, 4)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(layout)

    def update_value(self, msgpair: MsgPairModel):
        self.msgpair = msgpair
        self.event = self.msgpair.event
        self.reaction = self.msgpair.reaction

        self.input_emotion_name_label.setText(
            config.LANG_CONFIG_PARSER['emotion words'][
                self.event.emotion_label.name])

        self.output_emotion_name_label.setText(
            config.LANG_CONFIG_PARSER['emotion words'][
                self.reaction.emotion_label.name])

        self.input_emotion_value_label.setText(str(self.event.emotion_value))
        self.output_emotion_value_label.setText(str(self.reaction.emotion_value))
        self.input_description.setText(self.event.message)
        self.output_description.setText('"' + self.reaction.message + '"')
        self.repaint()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     font = QFont()
#     # font.setPixelSize(18)
#     app.setFont(font)
#     window = DialogsWidget()
#     window.show()
#     sys.exit(app.exec_())
