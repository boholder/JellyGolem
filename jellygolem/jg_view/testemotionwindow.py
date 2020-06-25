#!/usr/bin/python3
'''
@File : testemotionwindow.py

@Time : 2020/6/8

@Author : Boholder

@Function : Main frame for this package, using PyQt5.

'''

import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                             QSlider, QVBoxLayout, QWidget, QMainWindow,
                             QDoubleSpinBox, QLayout, QComboBox, QGroupBox,
                             QGridLayout, QSizePolicy)

from jellygolem.jg_view.emotionbtngroupwidget import EmotionButtonGroupWidget
from jellygolem.jg_view.robotstatewidget import RobotStateWidget
from jellygolem.jg_view.wheelpaintwidget import WheelPaintWidget
from jellygolem.jg_view.dialogswidget import DialogsWidget

import jellygolem.jg_emotion.emotionwheelprocess as emotionproc
from jellygolem.jg_emotion.robotemotionmodel import RobotEmotionData
from jellygolem.jg_emotion.robotemotionmodel import RobotEmotionModel
from jellygolem.jg_emotion.emotionwheelprocess import EmotionEnum
import jellygolem.jg_emotion.emotionreactiondriver as driver


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
        self.dialogs = DialogsWidget(EmotionEnum.BLANK,
                                     driver.get_event_by_emotion(EmotionEnum.BLANK),
                                     EmotionEnum.BLANK,
                                     driver.get_reaction_by_emotion(EmotionEnum.BLANK))

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

    def get_emotion_signal(self, emotion: EmotionEnum):
        try:
            # send signal to widgets
            displayed_emotion = self.processor.receive_emotion(emotion.value)
            internal_emotion = self.processor.emotion
            self.wheel.repaint_wheel(internal_emotion)

            # loglike
            print("robot receive: " + str(emotion) + str(emotion.value))
            print("robot display: " + str(displayed_emotion))
            print("robot internal: " + str(internal_emotion))

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
    window.show()
    sys.exit(app.exec_())
