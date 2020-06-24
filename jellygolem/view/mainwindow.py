#!/usr/bin/python3
'''
@File : mainwindow.py

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

from jellygolem.view.emotionbtngroupwidget import EmotionButtonGroupWidget
from jellygolem.view.robotstatewidget import RobotStateWidget
from jellygolem.view.wheelpaintwidget import WheelPaintWidget
from jellygolem.view.dialogswidget import DialogsWidget

from jellygolem.emotion.emotionwheelprocess import EmotionEnum
import jellygolem.emotion.emotionreactiondriver as driver


class MainWindow(QDialog):

    def __init__(self, name: str, favorability: int, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.btngroup = EmotionButtonGroupWidget()
        self.robotstate = RobotStateWidget(name, favorability, (0, 0))
        self.wheel = WheelPaintWidget((0, 0))
        self.dialogs = DialogsWidget(EmotionEnum.BLANK,
                                     driver.get_event_by_emotion(EmotionEnum.BLANK),
                                     EmotionEnum.BLANK,
                                     driver.get_reaction_by_emotion(EmotionEnum.BLANK))

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow('Tara', 20)
    window.show()
    sys.exit(app.exec_())
