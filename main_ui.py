# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# Главный скрипт, который запускает интерфейс программы

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget

from ui_editor.signs_ui import Ui_available_signs
from ui_editor.about_ui import Ui_About

from api.webcam_prediction import camera_start


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(500, 400)
        Form.move(QDesktopWidget().availableGeometry().center() - Form.frameGeometry().center())  # перемещаем окно в центр экрана
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 250, 300, 130))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Создание кнопки "Let's Talk" для перехода к работе с программой
        self.start_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)

        # Создание кнопки "About"
        self.button_about = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_about.setObjectName("button_about")
        self.verticalLayout.addWidget(self.button_about)

        # Создание кнопки "Available signs"
        self.button_signs = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_signs.setObjectName("button_signs")
        self.verticalLayout.addWidget(self.button_signs)

        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(50, 10, 400, 220))
        self.picture.setText("")
        self.picture.setTextFormat(QtCore.Qt.AutoText)
        self.picture.setPixmap(QtGui.QPixmap("pictures/lt.jpg"))
        self.picture.setScaledContents(True)
        self.picture.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.picture.setWordWrap(False)
        self.picture.setObjectName("picture")
        # По нажатию кнопки "Let's Talk" (start_button) произойдет запуск функции "camera_start"
        # И откроется окно для работы с моделью и видеокамерой
        self.start_button.clicked.connect(camera_start)

        # По нажатию кнопки "Available signs" (button_about) откроется новое окно с инструкцией, как пользоваться программой
        self.button_signs.clicked.connect(self.sign_window)

        # По нажатию кнопки "About" (button_about) откроется новое окно со списком знаков, которые обучена распознавать модель
        self.button_about.clicked.connect(self.about_window)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def about_window(self):
        self.About = QtWidgets.QWidget()
        self.ui = Ui_About()
        self.ui.setupUi(self.About)
        self.About.show()

    def sign_window(self):
        self.Sign = QtWidgets.QWidget()
        self.ui = Ui_available_signs()
        self.ui.setupUi(self.Sign)
        self.Sign.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Let\'s talk - ASL sign recognition"))
        self.start_button.setText(_translate("Form", "Let\'s Talk"))
        self.button_about.setText(_translate("Form", "About"))
        self.button_signs.setText(_translate("Form", "Available signs"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QTabWidget()
    ui = Ui_Form()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
