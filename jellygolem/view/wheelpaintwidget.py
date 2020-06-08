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
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtGui import QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel,
                             QSlider, QVBoxLayout, QWidget,
                             QDoubleSpinBox, QLayout)
import jellygolem.emotion.emotionwheelmodel as wheelmodel

RESOURCE_PATH = '../../resource/'
WHEEL_PIC_PATH = RESOURCE_PATH + 'emotion-wheel.png'
HEART_PIC_PATH = RESOURCE_PATH + 'heart.png'


class WheelPaintWidget(QWidget):
    value_changed_signal = pyqtSignal(float)

    def __init__(self, emotion, *args,
                 **kwargs):
        super(WheelPaintWidget, self).__init__(*args, **kwargs)

        self.emotion = emotion
        self.wheel_pixmap = QPixmap(WHEEL_PIC_PATH)
        self.heart_pixmap = QPixmap(HEART_PIC_PATH)

    def paintEvent(self, event: QtGui.QPaintEvent):
        super(WheelPaintWidget, self).paintEvent(event)
        self.setGeometry(self.geometry().x(), self.geometry().y(), 650, 650)
        (x, y) = wheelmodel.clac_paint_position(*self.emotion)
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.wheel_pixmap)
        painter.drawPixmap(x, y, 16, 16, self.heart_pixmap)


if __name__ == '__main__':
    app = QApplication([])
    ex = WheelPaintWidget((0, 0.2))
    ex.show()
    sys.exit(app.exec_())
