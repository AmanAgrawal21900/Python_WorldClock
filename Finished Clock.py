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
        self.lcdNumber.setGeometry(QtCore.QRect(10, 100, 371, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setDigitCount(12)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
