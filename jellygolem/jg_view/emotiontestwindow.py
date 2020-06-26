#!/usr/bin/python3
'''
@File : emotiontestwindow.py

@Time : 2020/6/8

@Author : Boholder

@Function : Main frame for this package, using PyQt5.

'''

import sys

from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy)

import jellygolem.jg_emotion.reactionstub as stub
import jellygolem.jg_emotion.emotionwheelprocess as emotionproc
from jellygolem.jg_conversation.messagemodel import MsgPairModel, MsgModel
from jellygolem.jg_emotion.emotionwheelprocess import EmotionEnum
from jellygolem.jg_emotion.robotemotionmodel import RobotEmotionData
from jellygolem.jg_emotion.robotemotionmodel import RobotEmotionModel
from jellygolem.jg_view.dialogswidget import DialogsWidget
from jellygolem.jg_view.emotionbtngroupwidget import EmotionButtonGroupWidget
from jellygolem.jg_view.robotstatewidget import RobotStateWidget
from jellygolem.jg_view.wheelpaintwidget import WheelPaintWidget


class MainWindow(QDialog):

    def __init__(self, name: str = 'RobotName',
                 initdata: RobotEmotionData = RobotEmotionData(),
                 emotionmodel: RobotEmotionModel = RobotEmotionModel(),
                 *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # init components
        self.btngroup = EmotionButtonGroupWidget()
        self.robotstate = RobotStateWidget(name, initdata.favorability, initdata.emotion)
        self.wheel = WheelPaintWidget(initdata.emotion)
        self.dialogs = DialogsWidget()

        # init an emotion model to store emotion
        self.processor = emotionmodel

        self.btngroup.emotion_signal.connect(self.get_emotion_signal)

        toplayout = QHBoxLayout()
        toplayout.addWidget(self.btngroup)
        toplayout.addWidget(self.wheel)
        toplayout.addWidget(QWidget())

        btmlayout = QHBoxLayout()
        btmlayout.addWidget(self.robotstate)
        btmlayout.addWidget(self.dialogs)
        btmlayout.addWidget(QWidget())

        layout = QVBoxLayout()
        layout.addLayout(toplayout)
        layout.addLayout(btmlayout)
        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)

    def get_emotion_signal(self, event_emotion: EmotionEnum):
        try:
            displayed_emotion = self.processor.receive_emotion(event_emotion.value)
            internal_emotion = self.processor.emotion
            favorability = self.processor.favorability

            # trigger widgets update methods
            self.wheel.repaint_wheel(internal_emotion)
            self.robotstate.update_value(favorability, internal_emotion)
            new_msgpair = MsgPairModel(
                MsgModel(event_emotion.value, stub.get_event_by_emotion(event_emotion)),
                MsgModel(displayed_emotion, stub.get_reaction_by_emotion(
                    emotionproc.find_closest_label(*displayed_emotion))))
            self.dialogs.update_value(new_msgpair)

            # # loglike
            # print("robot receive: " + str(emotion) + str(emotion.value))
            # print("robot display: " + str(displayed_emotion))
            # print("robot internal: " + str(internal_emotion))

        except Exception as e:
            raise e
        except ZeroDivisionError as e:
            raise e
        except ValueError as e:
            raise e


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.setWindowTitle('EmotionProcessingTest')
    window.show()
    sys.exit(app.exec_())
