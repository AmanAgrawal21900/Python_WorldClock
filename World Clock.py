# Importing Modules
import sys
import time
from pytz import all_timezones, timezone
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Ui_Form(object):

    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.current_time)
        self.timer.start(1000)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 180)
        Form.setMaximumSize(QtCore.QSize(420, 182))

        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 70, 381, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(12)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 11, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "World Clock"))
        self.label.setText(_translate("Form", "Asia/Kolkata"))

        # Adding Items to Combobox
        self.comboBox.clear()
        self.comboBox.addItems(all_timezones)
        self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(all_timezones.index("Asia/Kolkata"))
        self.comboBox.currentIndexChanged.connect(self.change_country)

    def current_time(self):
        current = time.strftime("%H : %M : %S")
        self.lcdNumber.display(current)
        self.change_country()

    def change_country(self):
        index = self.comboBox.currentIndex()
        self.label.setText(all_timezones[index])
        utc_time = datetime.now(timezone('UTC'))
        new_time = utc_time.astimezone(timezone(all_timezones[index]))
        print(new_time.strftime("%H : %M : %S"))
        self.lcdNumber.display(new_time.strftime("%H : %M : %S"))


# Main Program
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
