#!/usr/bin/python3
'''
@File : mainframe.py

@Time : 2020/6/8

@Author : Boholder

@Function : Main frame for this package, using PyQt5.

'''

import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                             QSlider, QVBoxLayout, QWidget, QMainWindow,
                             QDoubleSpinBox, QLayout, QComboBox, QGroupBox,
                             QGridLayout, QSizePolicy)


class MainWindow(QDialog):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
