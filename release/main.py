import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
import sqlite3
from release.addEditCoffeeForm import Ui_Form
from release.mainui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        # self.tableWidget = QTableWidget()

        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.addWindow)
        self.table_init()
        self.addAlltotable()

    def addAlltotable(self):
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect("data\coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM coffee WHERE id>0").fetchall()
        for row, cof in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for col, d in enumerate(cof):
                if col == 3:
                    if str(d) == '1':
                        d = 'молотый'
                    elif str(d) == '2':
                        d = 'в зернах'
                if d is not None:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(d)))
                else:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(''))

        self.tableWidget.resizeColumnsToContents()

    def table_init(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])

        self.tableWidget.resizeColumnsToContents()

    def addWindow(self):
        self.addw = AddWindow(self)
        self.addw.show()


class AddWindow(QWidget, Ui_Form):
    def __init__(self, mainW):
        self.MainW = mainW
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.save_btn.clicked.connect(self.save)
        self.add_btn.clicked.connect(self.add)
        self.table_init()
        self.addAlltotable()

    def addAlltotable(self):
        con = sqlite3.connect("data\coffee.sqlite")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM coffee WHERE id>0").fetchall()
        for row, cof in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for col, d in enumerate(cof[1:]):
                if col == 2:
                    if str(d) == '1':
                        d = 'молотый'
                    elif str(d) == '2':
                        d = 'в зернах'
                if d is not None:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(d)))
                else:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(''))

        self.tableWidget.resizeColumnsToContents()

    def table_init(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(
            ['название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])

        self.tableWidget.resizeColumnsToContents()

    def save(self):
        #   self.tableWidget = QTableWidget(self)
        titles = ['name', 'degree', 'type', 'taste', 'price', 'volume']
        self.cleanDB()

        for row in range(self.tableWidget.rowCount() + 1):
            data = {}
            for col in range(self.tableWidget.columnCount() + 1):
                item = self.tableWidget.item(row, col)
                if item is not None and item.text() != '':
                    data[titles[col]] = item.text()

            keys, vals = list(data.keys()), list(data.values())
            for i in range(len(keys)):
                if keys[i] in ('name', 'taste', 'degree', 'volume'):
                    vals[i] = "'" + vals[i] + "'"
                if keys[i] == 'type':
                    if vals[i] == 'молотый':
                        vals[i] = '1'
                    elif vals[i] == 'в зернах':
                        vals[i] = '2'

            if keys != []:
                s = f"INSERT INTO coffee({', '.join(keys)}) VALUES ({', '.join(vals)})"
                self.toDB(s)

        self.MainW.addAlltotable()
        self.close()

    def cleanDB(self):
        con = sqlite3.connect("data\coffee.sqlite")
        with con:
            cur = con.cursor()
            cur.execute("DELETE from coffee WHERE id>0")

    def toDB(self, sql_string):
        con = sqlite3.connect("data\coffee.sqlite")
        cur = con.cursor()
        with con:
            cur.execute(sql_string)

    def add(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)


app = QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec())
