# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DynoControlPanel(object):
    def setupUi(self, DynoControlPanel):
        DynoControlPanel.setObjectName(_fromUtf8("DynoControlPanel"))
        DynoControlPanel.resize(1024, 788)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DynoControlPanel.sizePolicy().hasHeightForWidth())
        DynoControlPanel.setSizePolicy(sizePolicy)
        DynoControlPanel.setMinimumSize(QtCore.QSize(1024, 768))
        DynoControlPanel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtGui.QWidget(DynoControlPanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalWidget_2 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(160, 200))
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(150, 600))
        self.verticalWidget_2.setObjectName(_fromUtf8("verticalWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.line_11 = QtGui.QFrame(self.verticalWidget_2)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.verticalLayout.addWidget(self.line_11)
        self.disableButton = QtGui.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disableButton.setFont(font)
        self.disableButton.setObjectName(_fromUtf8("disableButton"))
        self.verticalLayout.addWidget(self.disableButton)
        self.line_4 = QtGui.QFrame(self.verticalWidget_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.rlButton = QtGui.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rlButton.setFont(font)
        self.rlButton.setObjectName(_fromUtf8("rlButton"))
        self.verticalLayout.addWidget(self.rlButton)
        self.RoadLoadLayout = QtGui.QGridLayout()
        self.RoadLoadLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.RoadLoadLayout.setContentsMargins(-1, -1, 0, -1)
        self.RoadLoadLayout.setObjectName(_fromUtf8("RoadLoadLayout"))
        self.label_2 = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.RoadLoadLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.RoadLoadLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.RoadLoadLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.c2Box = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.c2Box.setDecimals(3)
        self.c2Box.setSingleStep(0.001)
        self.c2Box.setObjectName(_fromUtf8("c2Box"))
        self.RoadLoadLayout.addWidget(self.c2Box, 3, 1, 1, 1)
        self.c1Box = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.c1Box.setDecimals(3)
        self.c1Box.setSingleStep(0.001)
        self.c1Box.setObjectName(_fromUtf8("c1Box"))
        self.RoadLoadLayout.addWidget(self.c1Box, 2, 1, 1, 1)
        self.jBox = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.jBox.setDecimals(3)
        self.jBox.setMinimum(0.001)
        self.jBox.setSingleStep(0.001)
        self.jBox.setProperty("value", 0.01)
        self.jBox.setObjectName(_fromUtf8("jBox"))
        self.RoadLoadLayout.addWidget(self.jBox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.RoadLoadLayout)
        self.line = QtGui.QFrame(self.verticalWidget_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.sButton = QtGui.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sButton.setFont(font)
        self.sButton.setObjectName(_fromUtf8("sButton"))
        self.verticalLayout.addWidget(self.sButton)
        self.speedSlider = QtGui.QSlider(self.verticalWidget_2)
        self.speedSlider.setMinimum(-625)
        self.speedSlider.setMaximum(625)
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName(_fromUtf8("speedSlider"))
        self.verticalLayout.addWidget(self.speedSlider)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.sBox = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.sBox.setMinimum(-625.0)
        self.sBox.setMaximum(625.0)
        self.sBox.setObjectName(_fromUtf8("sBox"))
        self.gridLayout.addWidget(self.sBox, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_6 = QtGui.QFrame(self.verticalWidget_2)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.profileButton = QtGui.QRadioButton(self.verticalWidget_2)
        self.profileButton.setObjectName(_fromUtf8("profileButton"))
        self.verticalLayout.addWidget(self.profileButton)
        self.browseButton = QtGui.QPushButton(self.verticalWidget_2)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.verticalLayout.addWidget(self.browseButton)
        self.csvEdit = QtGui.QLineEdit(self.verticalWidget_2)
        self.csvEdit.setObjectName(_fromUtf8("csvEdit"))
        self.verticalLayout.addWidget(self.csvEdit)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.startButton = QtGui.QPushButton(self.verticalWidget_2)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout_4.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtGui.QPushButton(self.verticalWidget_2)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout_4.addWidget(self.stopButton, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.line_2 = QtGui.QFrame(self.verticalWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_7 = QtGui.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.verticalWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.buckBox = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.buckBox.setMaximum(48.0)
        self.buckBox.setObjectName(_fromUtf8("buckBox"))
        self.gridLayout_2.addWidget(self.buckBox, 0, 1, 1, 1)
        self.iMaxBox = QtGui.QDoubleSpinBox(self.verticalWidget_2)
        self.iMaxBox.setMaximum(200.0)
        self.iMaxBox.setProperty("value", 200.0)
        self.iMaxBox.setObjectName(_fromUtf8("iMaxBox"))
        self.gridLayout_2.addWidget(self.iMaxBox, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.verticalWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_12 = QtGui.QLabel(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.line_12 = QtGui.QFrame(self.verticalWidget)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.verticalLayout_2.addWidget(self.line_12)
        self.gridWidget = QtGui.QWidget(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_17 = QtGui.QLabel(self.gridWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_5.addWidget(self.label_17, 2, 1, 1, 1)
        self.testVMaxBox = QtGui.QDoubleSpinBox(self.gridWidget)
        self.testVMaxBox.setMaximum(5.0)
        self.testVMaxBox.setSingleStep(0.1)
        self.testVMaxBox.setProperty("value", 5.0)
        self.testVMaxBox.setObjectName(_fromUtf8("testVMaxBox"))
        self.gridLayout_5.addWidget(self.testVMaxBox, 3, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.testVMinBox = QtGui.QDoubleSpinBox(self.gridWidget)
        self.testVMinBox.setMaximum(5.0)
        self.testVMinBox.setSingleStep(0.1)
        self.testVMinBox.setObjectName(_fromUtf8("testVMinBox"))
        self.gridLayout_5.addWidget(self.testVMinBox, 3, 0, 1, 1)
        self.testVSetBox = QtGui.QDoubleSpinBox(self.gridWidget)
        self.testVSetBox.setMaximum(5.0)
        self.testVSetBox.setSingleStep(0.02)
        self.testVSetBox.setObjectName(_fromUtf8("testVSetBox"))
        self.gridLayout_5.addWidget(self.testVSetBox, 3, 2, 1, 1)
        self.label_25 = QtGui.QLabel(self.gridWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_5.addWidget(self.label_25, 2, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.gridWidget)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_5.addWidget(self.label_22, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget)
        self.line_8 = QtGui.QFrame(self.verticalWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_2.addWidget(self.line_8)
        self.gridWidget_2 = QtGui.QWidget(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget_2.setObjectName(_fromUtf8("gridWidget_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridWidget_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.periodMinBox = QtGui.QSpinBox(self.gridWidget_2)
        self.periodMinBox.setMaximum(2500)
        self.periodMinBox.setObjectName(_fromUtf8("periodMinBox"))
        self.gridLayout_6.addWidget(self.periodMinBox, 2, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_6.addWidget(self.label_19, 1, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.gridWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_6.addWidget(self.label_20, 1, 2, 1, 1)
        self.periodBox = QtGui.QSpinBox(self.gridWidget_2)
        self.periodBox.setMaximum(2500)
        self.periodBox.setSingleStep(5)
        self.periodBox.setObjectName(_fromUtf8("periodBox"))
        self.gridLayout_6.addWidget(self.periodBox, 2, 2, 1, 1)
        self.periodMaxBox = QtGui.QSpinBox(self.gridWidget_2)
        self.periodMaxBox.setMaximum(2500)
        self.periodMaxBox.setProperty("value", 2000)
        self.periodMaxBox.setObjectName(_fromUtf8("periodMaxBox"))
        self.gridLayout_6.addWidget(self.periodMaxBox, 2, 1, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridWidget_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget_2)
        self.line_9 = QtGui.QFrame(self.verticalWidget)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_2.addWidget(self.line_9)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_23 = QtGui.QLabel(self.verticalWidget)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_7.addWidget(self.label_23, 1, 1, 1, 1)
        self.canMinBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.canMinBox.setMinimum(-20.0)
        self.canMinBox.setMaximum(20.0)
        self.canMinBox.setSingleStep(0.01)
        self.canMinBox.setObjectName(_fromUtf8("canMinBox"))
        self.gridLayout_7.addWidget(self.canMinBox, 3, 0, 1, 1)
        self.canMaxBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.canMaxBox.setMinimum(-20.0)
        self.canMaxBox.setMaximum(20.0)
        self.canMaxBox.setSingleStep(0.01)
        self.canMaxBox.setObjectName(_fromUtf8("canMaxBox"))
        self.gridLayout_7.addWidget(self.canMaxBox, 3, 1, 1, 1)
        self.canBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.canBox.setMinimum(-20.0)
        self.canBox.setMaximum(20.0)
        self.canBox.setSingleStep(0.01)
        self.canBox.setObjectName(_fromUtf8("canBox"))
        self.gridLayout_7.addWidget(self.canBox, 3, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.verticalWidget)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_7.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.verticalWidget)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_7.addWidget(self.label_27, 2, 1, 1, 1)
        self.label_28 = QtGui.QLabel(self.verticalWidget)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_7.addWidget(self.label_28, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.line_10 = QtGui.QFrame(self.verticalWidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.verticalLayout_2.addWidget(self.line_10)
        self.label_24 = QtGui.QLabel(self.verticalWidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.verticalLayout_2.addWidget(self.label_24)
        self.line_7 = QtGui.QFrame(self.verticalWidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_2.addWidget(self.line_7)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.logButton = QtGui.QRadioButton(self.verticalWidget)
        self.logButton.setAutoExclusive(False)
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.verticalLayout_2.addWidget(self.logButton)
        self.filenameEdit = QtGui.QLineEdit(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.verticalLayout_2.addWidget(self.filenameEdit)
        self.line_13 = QtGui.QFrame(self.verticalWidget)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.verticalLayout_2.addWidget(self.line_13)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridWidget1 = QtGui.QWidget(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget1.sizePolicy().hasHeightForWidth())
        self.gridWidget1.setSizePolicy(sizePolicy)
        self.gridWidget1.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget1.setObjectName(_fromUtf8("gridWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridWidget1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.torqueText = QtGui.QLabel(self.gridWidget1)
        self.torqueText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.torqueText.setObjectName(_fromUtf8("torqueText"))
        self.gridLayout_3.addWidget(self.torqueText, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.speedText = QtGui.QLabel(self.gridWidget1)
        self.speedText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedText.setObjectName(_fromUtf8("speedText"))
        self.gridLayout_3.addWidget(self.speedText, 1, 1, 1, 1)
        self.voltageText = QtGui.QLabel(self.gridWidget1)
        self.voltageText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltageText.setObjectName(_fromUtf8("voltageText"))
        self.gridLayout_3.addWidget(self.voltageText, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 1)
        self.currentText = QtGui.QLabel(self.gridWidget1)
        self.currentText.setTextFormat(QtCore.Qt.AutoText)
        self.currentText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentText.setObjectName(_fromUtf8("currentText"))
        self.gridLayout_3.addWidget(self.currentText, 4, 1, 1, 1)
        self.mpText = QtGui.QLabel(self.gridWidget1)
        self.mpText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mpText.setObjectName(_fromUtf8("mpText"))
        self.gridLayout_3.addWidget(self.mpText, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridWidget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridWidget1)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 5, 0, 1, 1)
        self.epText = QtGui.QLabel(self.gridWidget1)
        self.epText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.epText.setObjectName(_fromUtf8("epText"))
        self.gridLayout_3.addWidget(self.epText, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget1)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalWidget1 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget1.sizePolicy().hasHeightForWidth())
        self.verticalWidget1.setSizePolicy(sizePolicy)
        self.verticalWidget1.setMinimumSize(QtCore.QSize(512, 0))
        self.verticalWidget1.setObjectName(_fromUtf8("verticalWidget1"))
        self.PlotLayout = QtGui.QVBoxLayout(self.verticalWidget1)
        self.PlotLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.PlotLayout.setObjectName(_fromUtf8("PlotLayout"))
        self.PlotLayout_2 = QtGui.QVBoxLayout()
        self.PlotLayout_2.setObjectName(_fromUtf8("PlotLayout_2"))
        self.PlotLayout.addLayout(self.PlotLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget1)
        DynoControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(DynoControlPanel)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DynoControlPanel.setStatusBar(self.statusbar)

        self.retranslateUi(DynoControlPanel)
        QtCore.QMetaObject.connectSlotsByName(DynoControlPanel)

    def retranslateUi(self, DynoControlPanel):
        DynoControlPanel.setWindowTitle(_translate("DynoControlPanel", "Dyno Control Panel", None))
        self.label_5.setText(_translate("DynoControlPanel", "Absorber Control", None))
        self.disableButton.setText(_translate("DynoControlPanel", "Disable", None))
        self.rlButton.setText(_translate("DynoControlPanel", "Road Load Mode", None))
        self.label_2.setText(_translate("DynoControlPanel", "C1", None))
        self.label.setText(_translate("DynoControlPanel", "C2", None))
        self.label_3.setText(_translate("DynoControlPanel", "J", None))
        self.sButton.setText(_translate("DynoControlPanel", "Manual Speed Mode", None))
        self.label_4.setText(_translate("DynoControlPanel", "Speed (rad/s)", None))
        self.profileButton.setText(_translate("DynoControlPanel", "Profile Mode", None))
        self.browseButton.setText(_translate("DynoControlPanel", "Browse for CSV", None))
        self.startButton.setText(_translate("DynoControlPanel", "Start", None))
        self.stopButton.setText(_translate("DynoControlPanel", "Stop", None))
        self.label_7.setText(_translate("DynoControlPanel", "Buck Control", None))
        self.label_6.setText(_translate("DynoControlPanel", "Voltage", None))
        self.label_9.setText(_translate("DynoControlPanel", "Max Current", None))
        self.label_12.setText(_translate("DynoControlPanel", "Test Motor Control", None))
        self.label_17.setText(_translate("DynoControlPanel", "Max V", None))
        self.label_16.setText(_translate("DynoControlPanel", "Min V", None))
        self.label_25.setText(_translate("DynoControlPanel", "Set V", None))
        self.label_22.setText(_translate("DynoControlPanel", "Analog", None))
        self.label_18.setText(_translate("DynoControlPanel", "Min us", None))
        self.label_19.setText(_translate("DynoControlPanel", "Max us", None))
        self.label_20.setText(_translate("DynoControlPanel", "Set us", None))
        self.label_21.setText(_translate("DynoControlPanel", "RC PWM", None))
        self.label_23.setText(_translate("DynoControlPanel", "CAN", None))
        self.label_26.setText(_translate("DynoControlPanel", "Min Torque", None))
        self.label_27.setText(_translate("DynoControlPanel", "Max Torque", None))
        self.label_28.setText(_translate("DynoControlPanel", "Set Torque", None))
        self.label_24.setText(_translate("DynoControlPanel", "Serial", None))
        self.logButton.setText(_translate("DynoControlPanel", "Log Data", None))
        self.torqueText.setText(_translate("DynoControlPanel", "0", None))
        self.label_8.setText(_translate("DynoControlPanel", "Torque (N-m)", None))
        self.speedText.setText(_translate("DynoControlPanel", "0", None))
        self.voltageText.setText(_translate("DynoControlPanel", "0", None))
        self.label_13.setText(_translate("DynoControlPanel", "DC Voltage (V)", None))
        self.label_15.setText(_translate("DynoControlPanel", "DC Current (A)", None))
        self.currentText.setText(_translate("DynoControlPanel", "0", None))
        self.mpText.setText(_translate("DynoControlPanel", "0", None))
        self.label_10.setText(_translate("DynoControlPanel", "Mechanical Power", None))
        self.label_11.setText(_translate("DynoControlPanel", "Speed (Rad/s)", None))
        self.label_14.setText(_translate("DynoControlPanel", "Electrical Power", None))
        self.epText.setText(_translate("DynoControlPanel", "0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DynoControlPanel = QtGui.QMainWindow()
    ui = Ui_DynoControlPanel()
    ui.setupUi(DynoControlPanel)
    DynoControlPanel.show()
    sys.exit(app.exec_())

