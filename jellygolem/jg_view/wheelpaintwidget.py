#!/usr/bin/python3
'''
@File : wheelpaintwidget.py

@Time : 2020/6/8

@Author : Boholder

@Function : Paint given emotion's position on emotion wheel picture,
            then display it in a widget.
'''

import sys

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget)

import jellygolem.jg_emotion.emotionwheelprocess as emotionproc

_RESOURCE_PATH = '../resource/'
_WHEEL_PIC_PATH = _RESOURCE_PATH + 'emotion-wheel.png'
_HEART_PIC_PATH = _RESOURCE_PATH + 'heart.png'


class WheelPaintWidget(QWidget):
    value_changed_signal = pyqtSignal(float)

    def __init__(self, emotion: tuple = (0, 0), *args,
                 **kwargs):
        super(WheelPaintWidget, self).__init__(*args, **kwargs)

        self.emotion = emotion
        self.wheel_pixmap = QPixmap(_WHEEL_PIC_PATH)
        self.heart_pixmap = QPixmap(_HEART_PIC_PATH)
        # if not so, when use this widget, it has no default space to show.
        self.setMinimumSize(self.wheel_pixmap.size())

    def paintEvent(self, event: QtGui.QPaintEvent):
        super(WheelPaintWidget, self).paintEvent(event)
        self.setGeometry(self.geometry().x(), self.geometry().y(), 650, 650)
        (x, y) = emotionproc.calc_paint_position(*self.emotion)
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.wheel_pixmap)
        painter.drawPixmap(x, y, 16, 16, self.heart_pixmap)

    def repaint_wheel(self, emotion: tuple):
        self.emotion = emotion
        self.repaint()

# if __name__ == '__main__':
#     app = QApplication([])
#     ex = WheelPaintWidget()
#     ex.show()
#     sys.exit(app.exec_())
