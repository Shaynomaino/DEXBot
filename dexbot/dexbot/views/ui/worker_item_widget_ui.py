# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jacko/Desktop/DEXBot/dexbot/dexbot/views/ui/worker_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(333, 292)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        widget.setFont(font)
        widget.setStyleSheet("background-color: #3A6257;\n"
"color: #ffffff;\n"
"border-radius: 20px;\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_5 = QtWidgets.QWidget(widget)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.widget_5.setFont(font)
        self.widget_5.setStyleSheet("border-radius: 20px;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NameStrategy = QtWidgets.QWidget(self.widget_5)
        self.NameStrategy.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.NameStrategy.setFont(font)
        self.NameStrategy.setStyleSheet("")
        self.NameStrategy.setObjectName("NameStrategy")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.NameStrategy)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.worker_name_label = QtWidgets.QLabel(self.NameStrategy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.worker_name_label.sizePolicy().hasHeightForWidth())
        self.worker_name_label.setSizePolicy(sizePolicy)
        self.worker_name_label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.worker_name_label.setFont(font)
        self.worker_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.worker_name_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.worker_name_label.setObjectName("worker_name_label")
        self.horizontalLayout.addWidget(self.worker_name_label)
        self.label_3 = QtWidgets.QLabel(self.NameStrategy)
        self.label_3.setMinimumSize(QtCore.QSize(10, 16))
        self.label_3.setMaximumSize(QtCore.QSize(10, 16))
        self.label_3.setStyleSheet("margin-top: 9px;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/worker_widget/svg/simplestrategy.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.strategy_label = QtWidgets.QLabel(self.NameStrategy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strategy_label.sizePolicy().hasHeightForWidth())
        self.strategy_label.setSizePolicy(sizePolicy)
        self.strategy_label.setMaximumSize(QtCore.QSize(16777215, 16777042))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.strategy_label.setFont(font)
        self.strategy_label.setStyleSheet("margin-top: 9px;")
        self.strategy_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.strategy_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.strategy_label.setObjectName("strategy_label")
        self.horizontalLayout.addWidget(self.strategy_label)
        self.verticalLayout.addWidget(self.NameStrategy)
        self.line = QtWidgets.QFrame(self.widget_5)
        self.line.setEnabled(True)
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setStyleSheet("background: black;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget_2 = QtWidgets.QWidget(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.profit_range_label = QtWidgets.QLabel(self.widget_2)
        self.profit_range_label.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.profit_range_label.setFont(font)
        self.profit_range_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.profit_range_label.setObjectName("profit_range_label")
        self.horizontalLayout_3.addWidget(self.profit_range_label)
        self.profit_label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.profit_label.setFont(font)
        self.profit_label.setStyleSheet("color: #99F75C;")
        self.profit_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.profit_label.setObjectName("profit_label")
        self.horizontalLayout_3.addWidget(self.profit_label)
        self.currency_label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.currency_label.setFont(font)
        self.currency_label.setText("")
        self.currency_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currency_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.currency_label.setObjectName("currency_label")
        self.horizontalLayout_3.addWidget(self.currency_label)
        self.verticalLayout.addWidget(self.widget_2)
        self.bar = QtWidgets.QWidget(self.widget_5)
        self.bar.setMinimumSize(QtCore.QSize(280, 30))
        self.bar.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.bar.setFont(font)
        self.bar.setStyleSheet("border-radius: 15px;\n"
"background: #ffffff;\n"
"max-height: 30px;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.bar.setObjectName("bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bar)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.base_asset_label = QtWidgets.QLabel(self.bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_asset_label.sizePolicy().hasHeightForWidth())
        self.base_asset_label.setSizePolicy(sizePolicy)
        self.base_asset_label.setMinimumSize(QtCore.QSize(20, 0))
        self.base_asset_label.setMaximumSize(QtCore.QSize(16777191, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.base_asset_label.setFont(font)
        self.base_asset_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.base_asset_label.setStyleSheet("background: #dfa93b;\n"
"border-radius: 10px; padding-left: 5px;")
        self.base_asset_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.base_asset_label.setObjectName("base_asset_label")
        self.horizontalLayout_2.addWidget(self.base_asset_label)
        self.quote_asset_label = QtWidgets.QLabel(self.bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_asset_label.sizePolicy().hasHeightForWidth())
        self.quote_asset_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.quote_asset_label.setFont(font)
        self.quote_asset_label.setStyleSheet("border-radius: 10px; padding-left: 5px; background: #6794ec; ")
        self.quote_asset_label.setObjectName("quote_asset_label")
        self.horizontalLayout_2.addWidget(self.quote_asset_label)
        self.verticalLayout.addWidget(self.bar, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("border-radius: 0px;")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.running = QtWidgets.QWidget(self.widget_3)
        self.running.setMinimumSize(QtCore.QSize(0, 60))
        self.running.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.running.setFont(font)
        self.running.setObjectName("running")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.running)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.onoff = QtWidgets.QWidget(self.running)
        self.onoff.setMinimumSize(QtCore.QSize(50, 24))
        self.onoff.setMaximumSize(QtCore.QSize(50, 24))
        self.onoff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.onoff.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.onoff.setStyleSheet("border-radius: 12px;\n"
"background: #ffffff;\n"
"max-height: 24px;\n"
"padding: 0px;\n"
"margin: 0px;")
        self.onoff.setObjectName("onoff")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.onoff)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toggle = QtWidgets.QWidget(self.onoff)
        self.toggle.setMinimumSize(QtCore.QSize(20, 20))
        self.toggle.setMaximumSize(QtCore.QSize(20, 24))
        self.toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toggle.setStyleSheet("background-color: #3A6257; border-radius: 10px;float:right;")
        self.toggle.setObjectName("toggle")
        self.horizontalLayout_5.addWidget(self.toggle, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.onoff, 0, QtCore.Qt.AlignHCenter)
        self.toggle_label = QtWidgets.QLabel(self.running)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.toggle_label.setFont(font)
        self.toggle_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.toggle_label.setObjectName("toggle_label")
        self.verticalLayout_3.addWidget(self.toggle_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.running)
        self.details = QtWidgets.QWidget(self.widget_3)
        self.details.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.details.setFont(font)
        self.details.setObjectName("details")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.details)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.details_button = QtWidgets.QPushButton(self.details)
        self.details_button.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.details_button.setFont(font)
        self.details_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.details_button.setStyleSheet("color: #ffffff")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/worker_widget/img/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.details_button.setIcon(icon)
        self.details_button.setIconSize(QtCore.QSize(30, 30))
        self.details_button.setFlat(True)
        self.details_button.setObjectName("details_button")
        self.verticalLayout_6.addWidget(self.details_button)
        self.details_label = QtWidgets.QLabel(self.details)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.details_label.setFont(font)
        self.details_label.setStyleSheet("")
        self.details_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.details_label.setObjectName("details_label")
        self.verticalLayout_6.addWidget(self.details_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.details)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.widget_4.setFont(font)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.edit_button = QtWidgets.QPushButton(self.widget_4)
        self.edit_button.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.edit_button.setFont(font)
        self.edit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_button.setStyleSheet("color: #ffffff")
        self.edit_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/worker_widget/svg/modifystrategy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon1)
        self.edit_button.setIconSize(QtCore.QSize(30, 30))
        self.edit_button.setFlat(True)
        self.edit_button.setObjectName("edit_button")
        self.verticalLayout_2.addWidget(self.edit_button)
        self.edit_label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.edit_label.setFont(font)
        self.edit_label.setStyleSheet("")
        self.edit_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.edit_label.setObjectName("edit_label")
        self.verticalLayout_2.addWidget(self.edit_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.worker_status = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setBold(True)
        font.setWeight(75)
        self.worker_status.setFont(font)
        self.worker_status.setAlignment(QtCore.Qt.AlignCenter)
        self.worker_status.setWordWrap(True)
        self.worker_status.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.worker_status.setObjectName("worker_status")
        self.verticalLayout.addWidget(self.worker_status)
        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.worker_name_label.setText(_translate("widget", "Bot name"))
        self.strategy_label.setText(_translate("widget", "SIMPLE STRATEGY"))
        self.profit_range_label.setText(_translate("widget", "(7d)"))
        self.profit_label.setText(_translate("widget", "+0.0%"))
        self.base_asset_label.setText(_translate("widget", "EUR"))
        self.quote_asset_label.setText(_translate("widget", "USD"))
        self.toggle_label.setText(_translate("widget", "TURN WORKER ON"))
        self.details_label.setText(_translate("widget", "DETAILS"))
        self.edit_label.setText(_translate("widget", "MODIFY WORKER"))
        self.worker_status.setText(_translate("widget", "Worker not running"))

from dexbot.resources import fonts_rc
from dexbot.resources import icons_rc
