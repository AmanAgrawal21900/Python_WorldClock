# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ccc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 255)
        Form.setMaximumSize(QtCore.QSize(420, 255))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 401, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.clock = QtWidgets.QWidget()
        self.clock.setObjectName("clock")
        self.comboBox = QtWidgets.QComboBox(self.clock)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 121, 21))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.clock)
        self.label.setGeometry(QtCore.QRect(70, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.clock)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 110, 371, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget.addTab(self.clock, "")
        self.calendar = QtWidgets.QWidget()
        self.calendar.setObjectName("calendar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 10, 328, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget.addTab(self.calendar, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "World Clock"))
        self.label.setText(_translate("Form", "Asia/Kolkata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clock), _translate("Form", "Clock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calendar), _translate("Form", "Calendar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
