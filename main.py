from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
'''
Команды для создания БД:

CREATE TABLE Lastname
(
    Id SERIAL PRIMARY KEY,
    lname VARCHAR(30) NOT NULL
);
CREATE TABLE Firstname
(
    Id SERIAL PRIMARY KEY,
    fname VARCHAR(30) NOT NULL
);
CREATE TABLE Otch
(
    Id SERIAL PRIMARY KEY,
    otc VARCHAR(30) NOT NULL
);

CREATE TABLE Town
(
    Id SERIAL PRIMARY KEY,
    town VARCHAR(30) NOT NULL
);
CREATE TABLE Book
(
    Id SERIAL PRIMARY KEY,
    LastnameId INTEGER NOT NULL REFERENCES Lastname(Id) ON DELETE CASCADE,
    FistnameId INTEGER NOT NULL REFERENCES Firstname(Id) ON DELETE CASCADE,
	OtchId INTEGER NOT NULL REFERENCES Otch(Id) ON DELETE CASCADE,
	TownId INTEGER NOT NULL REFERENCES Town(Id) ON DELETE CASCADE,
    Telef VARCHAR(30) NOT NULL,
    Street VARCHAR(30) NOT NULL,
	House VARCHAR(30) NOT NULL,
    Appr VARCHAR(30) NOT NULL
);
'''
import sys
from mainwindow import *
from famwindow import *

conn = psycopg2.connect(dbname='telebook', user='postgres', password='111', host='localhost')
cursor = conn.cursor()


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setRowCount(100)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Фамилия', 'Имя', 'Отчество', 'Город', 'Телефон', 'Улица', 'Дом', 'Квартира'))

        self.btnShowAll()

        self.ui.pushButton_6.clicked.connect(self.openFamDialog)
        self.dialog = mysecondwindow(self)

        self.ui.pushButton_7.clicked.connect(self.openNamDialog)
        self.dialog1 = mythirdwindow(self)

        self.ui.pushButton_8.clicked.connect(self.openOtcDialog)
        self.dialog2 = myfourdwindow(self)

        self.ui.pushButton_9.clicked.connect(self.openTownDialog)
        self.dialog3 = myfivewindow(self)

        self.update()

        self.ui.pushButton.clicked.connect(self.btnAdduser)

        self.ui.pushButton_2.clicked.connect(self.btnDeluser)

        self.ui.pushButton_3.clicked.connect(self.btnUpdateuser)

        self.ui.pushButton_4.clicked.connect(self.btnFinduser)

        self.ui.pushButton_5.clicked.connect(self.btnShowAll)

    def takeFam(self):
        '''Берёт все фамилии'''
        cursor.execute('''
                    SELECT Lname FROM Lastname 
                    ''')
        conn.commit()

        records = cursor.fetchall()

        data = []
        famlist = []
        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                famlist.append(item)
                col += 1

            row += 1

        return famlist

    def takeNam(self):
        '''Берёт все имена'''
        cursor.execute('''
                    SELECT Fname FROM Firstname 
                    ''')
        conn.commit()

        records = cursor.fetchall()

        data = []
        namlist = []
        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                namlist.append(item)
                col += 1

            row += 1

        return namlist

    def takeOtc(self):
        '''Берёт все отчества'''
        cursor.execute('''
                            SELECT Otc FROM Otch
                            ''')
        conn.commit()

        records = cursor.fetchall()

        data = []
        namlist = []
        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                namlist.append(item)
                col += 1

            row += 1

        return namlist

    def takeTown(self):
        '''Берёт все Города'''
        cursor.execute('''
                                    SELECT town FROM Town
                                    ''')
        conn.commit()

        records = cursor.fetchall()

        data = []
        townlist = []
        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                townlist.append(item)
                col += 1

            row += 1

        return townlist

    def openFamDialog(self):
        self.dialog.show()

    def openNamDialog(self):
        self.dialog1.show()

    def openOtcDialog(self):
        self.dialog2.show()

    def openTownDialog(self):
        self.dialog3.show()

    def btnAdduser(self):
        fam_сh = self.ui.comboBox.currentText()
        cursor.execute('''SELECT * FROM Lastname WHERE lname= '{}';'''.format(fam_сh))
        conn.commit()
        fam_int = int(cursor.fetchall()[0][0])
        nam_сh = self.ui.comboBox_2.currentText()
        cursor.execute('''SELECT * FROM Firstname WHERE fname= '{}';'''.format(nam_сh))
        conn.commit()
        nam_int = int(cursor.fetchall()[0][0])
        otc_сh = self.ui.comboBox_3.currentText()
        cursor.execute('''SELECT * FROM Otch WHERE otc= '{}';'''.format(otc_сh))
        conn.commit()
        otc_int = int(cursor.fetchall()[0][0])
        town_сh = self.ui.comboBox_4.currentText()
        cursor.execute('''SELECT * FROM Town WHERE town= '{}';'''.format(town_сh))
        conn.commit()
        town_int = int(cursor.fetchall()[0][0])

        telef = str(self.ui.lineEdit.text())
        street = str(self.ui.lineEdit_2.text())
        house = str(self.ui.lineEdit_3.text())
        appr = str(self.ui.lineEdit_4.text())

        print(
            "'{}','{}','{}','{}','{}','{}','{}','{}'".format(fam_int, nam_int, town_int, otc_int, telef, street, house,
                                                             appr))

        cursor.execute(
            '''INSERT INTO Book(LastnameId,FirstnameId,OtchId,TownId,telef,street,house,appr) VALUES ({},{},{},{},
            '{}','{}','{}','{}');'''.format(
                fam_int, nam_int, otc_int, town_int, telef, street, house, appr))
        conn.commit()

        self.btnShowAll()

    def btnDeluser(self):
        try:
            fam_сh = self.ui.comboBox.currentText()
            cursor.execute('''SELECT * FROM Lastname WHERE lname= '{}';'''.format(fam_сh))
            conn.commit()

            fam_int = int(cursor.fetchall()[0][0])
            nam_сh = self.ui.comboBox_2.currentText()
            cursor.execute('''SELECT * FROM Firstname WHERE fname= '{}';'''.format(nam_сh))
            conn.commit()

            nam_int = int(cursor.fetchall()[0][0])
            otc_сh = self.ui.comboBox_3.currentText()
            cursor.execute('''SELECT * FROM Otch WHERE otc= '{}';'''.format(otc_сh))
            conn.commit()

            otc_int = int(cursor.fetchall()[0][0])
            town_сh = self.ui.comboBox_4.currentText()
            cursor.execute('''SELECT * FROM Town WHERE town= '{}';'''.format(town_сh))
            conn.commit()

            town_int = int(cursor.fetchall()[0][0])
            telef = str(self.ui.lineEdit.text())
            street = str(self.ui.lineEdit_2.text())
            house = str(self.ui.lineEdit_3.text())
            appr = str(self.ui.lineEdit_4.text())

            command = '''DELETE FROM Book WHERE LastnameId={} AND FirstnameId={} AND OtchId={} AND TownId={} '''.format(
                fam_int, nam_int, otc_int, town_int)

            if not telef:
                pass
            else:
                command = command + "AND telef = '{}'".format(telef)
            if not street:
                pass
            else:
                command = command + "AND street = '{}'".format(street)
            if not house:
                pass
            else:
                command = command + "AND house = '{}'".format(house)
            if not appr:
                pass
            else:
                command = command + "AND appr = '{}'".format(appr)

            exc = command + ''';'''

            print(exc)

            cursor.execute(exc)
            conn.commit()
            self.btnShowAll()
        except:
            print('no')

    def btnUpdateuser(self):
        fam_сh = self.ui.comboBox.currentText()
        cursor.execute('''SELECT * FROM Lastname WHERE lname= '{}';'''.format(fam_сh))
        conn.commit()
        fam_int = int(cursor.fetchall()[0][0])
        nam_сh = self.ui.comboBox_2.currentText()
        cursor.execute('''SELECT * FROM Firstname WHERE fname= '{}';'''.format(nam_сh))
        conn.commit()
        nam_int = int(cursor.fetchall()[0][0])
        otc_сh = self.ui.comboBox_3.currentText()
        cursor.execute('''SELECT * FROM Otch WHERE otc= '{}';'''.format(otc_сh))
        conn.commit()
        otc_int = int(cursor.fetchall()[0][0])
        town_сh = self.ui.comboBox_4.currentText()
        cursor.execute('''SELECT * FROM Town WHERE town= '{}';'''.format(town_сh))
        conn.commit()
        town_int = int(cursor.fetchall()[0][0])

        telef = str(self.ui.lineEdit.text())
        street = str(self.ui.lineEdit_2.text())
        house = str(self.ui.lineEdit_3.text())
        appr = str(self.ui.lineEdit_4.text())

        command = ('''WHERE 
                         LastnameId={} 
                         AND 
                         FirstnameId={}
                         AND
                         OtchId={}
                         AND
                         TownId={} ''').format(fam_int, nam_int, otc_int, town_int)

        exc = ('''UPDATE Book SET telef ='{}' , street='{}' , house = '{}' , appr='{}' ''').format(telef, street, house,
                                                                                                   appr) + command + ''';'''

        cursor.execute(exc)
        conn.commit()

        self.btnShowAll()

    def btnFinduser(self):

        try:
            self.ui.tableWidget.clear()

            fam_сh = self.ui.comboBox.currentText()
            cursor.execute('''SELECT * FROM Lastname WHERE lname= '{}';'''.format(fam_сh))
            conn.commit()
            if not fam_сh:
                fam_int = None
            else:
                fam_int = int(cursor.fetchall()[0][0])

            nam_сh = self.ui.comboBox_2.currentText()
            cursor.execute('''SELECT * FROM Firstname WHERE fname= '{}';'''.format(nam_сh))
            conn.commit()
            if not nam_сh:
                nam_int = None
            else:
                nam_int = int(cursor.fetchall()[0][0])

            otc_сh = self.ui.comboBox_3.currentText()
            cursor.execute('''SELECT * FROM Otch WHERE otc= '{}';'''.format(otc_сh))
            conn.commit()
            if not otc_сh:
                otc_int = None
            else:
                otc_int = int(cursor.fetchall()[0][0])

            print(otc_int)

            town_сh = self.ui.comboBox_4.currentText()
            cursor.execute('''SELECT * FROM Town WHERE town= '{}';'''.format(town_сh))
            conn.commit()
            if not town_сh:
                town_int = None
            else:
                town_int = int(cursor.fetchall()[0][0])

            telef = str(self.ui.lineEdit.text())
            street = str(self.ui.lineEdit_2.text())
            house = str(self.ui.lineEdit_3.text())
            appr = str(self.ui.lineEdit_4.text())

            is_it_first = True

            command = ''' WHERE '''

            if fam_int != None:
                if is_it_first:
                    command = command + ' LastnameId={} '.format(fam_int)
                    is_it_first = False
                else:
                    command = command + ' AND LastnameId={} '.format(fam_int)
            if nam_int != None:
                if is_it_first:
                    command = command + ' FirstnameId={} '.format(nam_int)
                    is_it_first = False
                else:
                    command = command + ' AND FirstnameId={} '.format(nam_int)

            if otc_int != None:
                if is_it_first:
                    command = command + ' OtchId={} '.format(otc_int)
                    is_it_first = False
                else:
                    command = command + ' AND OtchId={} '.format(otc_int)
            if town_int != None:
                if is_it_first:
                    command = command + ' TownId={} '.format(town_int)
                    is_it_first = False
                else:
                    command = command + ' AND TownId={} '.format(town_int)
            if not telef:
                pass
            else:
                if is_it_first:
                    command = command + " telef = '{}'".format(telef)
                    is_it_first = False
                else:
                    command = command + "AND telef = '{}'".format(telef)
            if not street:
                pass
            else:
                if is_it_first:
                    command = command + "street = '{}'".format(street)
                    is_it_first = False
                else:
                    command = command + " AND street = '{}'".format(street)
            if not house:
                pass
            else:
                if is_it_first:
                    command = command + " house = '{}'".format(house)
                    is_it_first = False
                else:
                    command = command + " AND house = '{}'".format(house)
            if not appr:
                pass
            else:
                if is_it_first:
                    command = command + " appr = '{}'".format(appr)
                    is_it_first = False
                else:
                    command = command + " AND appr = '{}'".format(appr)

            exc = '''select Lastname.lname,Firstname.fname,Otch.otc,Town.town,Telef,Street,House,Appr
                        from Book
                        join Lastname on Lastname.Id = Book.LastnameId
                        join Firstname on Firstname.Id = Book.FirstnameId
                        join Otch on Otch.Id = Book.OtchId
                        join Town on Town.Id = Book.TownId ''' + command + ''';'''

            cursor.execute(exc)
            print(exc)
            conn.commit()
            records = cursor.fetchall()

            print(records)

            data = []

            for i in records:
                data.append(i)

            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(str(item))
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    col += 1

                row += 1

            self.ui.tableWidget.setColumnCount(8)
            self.ui.tableWidget.setRowCount(100)
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ('Фамилия', 'Имя', 'Отчество', 'Город', 'Телефон', 'Улица', 'Дом', 'Квартира'))
        except:
            print(otc_int)
            print(exc)
            print(records)

    def btnShowAll(self):

        self.ui.tableWidget.clear()

        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setRowCount(100)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Фамилия', 'Имя', 'Отчество', 'Город', 'Телефон', 'Улица', 'Дом', 'Квартира'))

        cursor.execute('''
        select Lastname.lname,Firstname.fname,Otch.otc,Town.town,Telef,Street,House,Appr
        from Book 
        join Lastname on Lastname.Id = Book.LastnameId
        join Firstname on Firstname.Id = Book.FirstnameId
        join Otch on Otch.Id = Book.OtchId
        join Town on Town.Id = Book.TownId''')
        conn.commit()

        records = cursor.fetchall()

        data = []

        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

        self.update()

    def update(self):
        self.ui.comboBox.clear()
        famlist = self.takeFam()
        self.ui.comboBox.addItem((''))
        self.ui.comboBox.addItems((famlist))

        self.ui.comboBox_2.clear()
        namlist = self.takeNam()
        self.ui.comboBox_2.addItem((''))
        self.ui.comboBox_2.addItems((namlist))

        self.ui.comboBox_3.clear()
        otclist = self.takeOtc()
        self.ui.comboBox_3.addItem((''))
        self.ui.comboBox_3.addItems((otclist))

        self.ui.comboBox_4.clear()
        townlist = self.takeTown()
        self.ui.comboBox_4.addItem((''))
        self.ui.comboBox_4.addItems((townlist))

        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

class mysecondwindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(mysecondwindow, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ShowAll()

        self.ui.pushButton.clicked.connect(self.famAdd)
        self.ui.pushButton_2.clicked.connect(self.famDel)

    def ShowAll(self):
        '''Показать всех пользователей'''

        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(10)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Фамилии', 'Dont touch'))
        cursor.execute('''
        SELECT Lname FROM Lastname 
        ''')
        conn.commit()

        records = cursor.fetchall()

        data = []

        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def famAdd(self):
        a = self.ui.lineEdit.text()
        cursor.execute('''INSERT INTO Lastname(lname) VALUES ('{}');'''.format(a))
        conn.commit()
        self.ShowAll()
        window.update()

    def famDel(self):
        a = self.ui.lineEdit.text()
        cursor.execute('''DELETE FROM Lastname WHERE Lname = '{}';'''.format(a))
        conn.commit()
        self.ShowAll()
        window.update()


class mythirdwindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(mythirdwindow, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ShowAll()

        self.ui.pushButton.clicked.connect(self.namAdd)
        self.ui.pushButton_2.clicked.connect(self.namDel)

    def ShowAll(self):
        '''Показать всех пользователей'''

        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(10)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Имена', 'Dont touch'))
        cursor.execute('''
        SELECT Fname FROM Firstname 
        ''')
        conn.commit()

        records = cursor.fetchall()

        data = []

        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def namAdd(self):

        a = self.ui.lineEdit.text()
        cursor.execute('''
                            INSERT INTO Firstname(fname)
                            VALUES ('{}');
                            '''.format(a))
        conn.commit()
        print('Был добавлен {}'.format(a))
        self.ShowAll()
        try:
            window.update()
            print('Обновилось')
        except:
            print('Не Обновилось')

    def namDel(self):

        a = self.ui.lineEdit.text()
        cursor.execute('''DELETE FROM Firstname
                          WHERE Fname = '{}';'''.format(a))
        conn.commit()
        print('Был удален {}'.format(a))
        self.ShowAll()
        window.update()


class myfourdwindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(myfourdwindow, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ShowAll()

        self.ui.pushButton.clicked.connect(self.otcAdd)
        self.ui.pushButton_2.clicked.connect(self.otcDel)

    def ShowAll(self):


        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(10)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Отчества', 'Dont touch'))
        cursor.execute('''
        SELECT Otc FROM Otch
        ''')
        conn.commit()

        records = cursor.fetchall()

        data = []

        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def otcAdd(self):

        a = self.ui.lineEdit.text()
        cursor.execute('''
                            INSERT INTO Otch(Otc)
                            VALUES ('{}');
                            '''.format(a))
        conn.commit()
        print('Был добавлен {}'.format(a))
        self.ShowAll()
        try:
            window.update()
            print('Обновилось')
        except:
            print('Не Обновилось')

    def otcDel(self):

        a = self.ui.lineEdit.text()
        cursor.execute('''DELETE FROM Otch
                          WHERE Otc = '{}';'''.format(a))
        conn.commit()
        print('Был удален {}'.format(a))
        self.ShowAll()
        window.update()


class myfivewindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(myfivewindow, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ShowAll()

        self.ui.pushButton.clicked.connect(self.TownAdd)
        self.ui.pushButton_2.clicked.connect(self.TownDel)

    def ShowAll(self):


        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(10)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Города', 'Dont touch'))
        cursor.execute('''
        SELECT town FROM Town
        ''')
        conn.commit()

        records = cursor.fetchall()

        data = []

        for i in records:
            data.append(i)

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    def TownAdd(self):

        a = self.ui.lineEdit.text()
        cursor.execute('''
                            INSERT INTO Town(town)
                            VALUES ('{}');
                            '''.format(a))
        conn.commit()
        print('Был добавлен {}'.format(a))
        self.ShowAll()
        try:
            window.update()
            print('Обновилось')
        except:
            print('Не Обновилось')

    def TownDel(self):
        
        a = self.ui.lineEdit.text()
        cursor.execute('''DELETE FROM Town
                          WHERE town = '{}';'''.format(a))
        conn.commit()
        print('Был удален {}'.format(a))
        self.ShowAll()
        window.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
