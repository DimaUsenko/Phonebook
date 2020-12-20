# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 657)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/icon_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(212, 209, 207, 1), stop:1 rgba(171, 208, 235, 1));\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 851, 321))
        self.tableWidget.setStyleSheet("color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";\n"
"")
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 400, 141, 22))
        self.comboBox.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 400, 141, 22))
        self.comboBox_2.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 400, 141, 22))
        self.comboBox_3.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(550, 400, 141, 22))
        self.comboBox_4.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 470, 161, 21))
        self.lineEdit.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 470, 161, 21))
        self.lineEdit_2.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 470, 61, 21))
        self.lineEdit_3.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 370, 81, 20))
        self.label.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 370, 41, 20))
        self.label_2.setStyleSheet("color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 370, 81, 20))
        self.label_3.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 370, 51, 20))
        self.label_4.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 440, 81, 20))
        self.label_5.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 440, 61, 20))
        self.label_6.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 440, 41, 20))
        self.label_7.setStyleSheet("color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 440, 91, 20))
        self.label_8.setStyleSheet("\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(450, 470, 91, 21))
        self.lineEdit_4.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 10pt \"Palatino Linotype\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 520, 151, 27))
        self.pushButton.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 560, 151, 27))
        self.pushButton_2.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 600, 151, 27))
        self.pushButton_3.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 520, 161, 27))
        self.pushButton_4.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 520, 161, 27))
        self.pushButton_5.setStyleSheet("\n"
"\n"
"color: #873f2d;\n"
"font: 14pt \"Palatino Linotype\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 400, 16, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 400, 16, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(520, 400, 16, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 400, 16, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phonebook"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.label_4.setText(_translate("MainWindow", "Город"))
        self.label_5.setText(_translate("MainWindow", "Телефон"))
        self.label_6.setText(_translate("MainWindow", "Улица"))
        self.label_7.setText(_translate("MainWindow", "Дом"))
        self.label_8.setText(_translate("MainWindow", "Квартира"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_3.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_4.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_5.setText(_translate("MainWindow", "Показать всех"))
        self.pushButton_6.setText(_translate("MainWindow", "."))
        self.pushButton_7.setText(_translate("MainWindow", "."))
        self.pushButton_8.setText(_translate("MainWindow", "."))
        self.pushButton_9.setText(_translate("MainWindow", "."))
