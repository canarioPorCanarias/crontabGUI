# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class crontab_gui():
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.setFixedSize(480, 640)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(200, 10, 91, 31))
        self.label.setObjectName("label")
        self.save_button = QtWidgets.QPushButton(Frame)
        self.save_button.setGeometry(QtCore.QRect(270, 590, 80, 23))
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(Frame)
        self.cancel_button.setGeometry(QtCore.QRect(360, 590, 80, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(20, 290, 421, 261))
        self.frame.setStyleSheet("#Frame{border:\"5px solid black\"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 311, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minute_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.minute_input.setObjectName("minute_input")
        self.horizontalLayout.addWidget(self.minute_input)
        self.hour_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.hour_input.setObjectName("hour_input")
        self.horizontalLayout.addWidget(self.hour_input)
        self.day_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.day_input.setObjectName("day_input")
        self.horizontalLayout.addWidget(self.day_input)
        self.month_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.month_input.setObjectName("month_input")
        self.horizontalLayout.addWidget(self.month_input)
        self.week_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.week_input.setObjectName("week_input")
        self.horizontalLayout.addWidget(self.week_input)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(20, 40, 311, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.add_button = QtWidgets.QPushButton(self.frame)
        self.add_button.setGeometry(QtCore.QRect(340, 70, 71, 23))
        self.add_button.setObjectName("add_button")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.label_7.setObjectName("label_7")
        self.command_input = QtWidgets.QLineEdit(self.frame)
        self.command_input.setGeometry(QtCore.QRect(20, 130, 311, 31))
        self.command_input.setObjectName("command_input")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 81, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 311, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 210, 80, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 0, 392, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startup = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.startup.setMaximumSize(QtCore.QSize(60, 23))
        self.startup.setCheckable(True)
        self.startup.setAutoExclusive(True)
        self.startup.setDefault(False)
        self.startup.setObjectName("startup")
        self.horizontalLayout_3.addWidget(self.startup)
        self.hourly = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.hourly.setMaximumSize(QtCore.QSize(60, 23))
        self.hourly.setCheckable(True)
        self.hourly.setAutoExclusive(True)
        self.hourly.setObjectName("hourly")
        self.horizontalLayout_3.addWidget(self.hourly)
        self.daily = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.daily.setMaximumSize(QtCore.QSize(60, 23))
        self.daily.setCheckable(True)
        self.daily.setAutoExclusive(True)
        self.daily.setObjectName("daily")
        self.horizontalLayout_3.addWidget(self.daily)
        self.weekly = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.weekly.setMaximumSize(QtCore.QSize(60, 23))
        self.weekly.setCheckable(True)
        self.weekly.setAutoExclusive(True)
        self.weekly.setObjectName("weekly")
        self.horizontalLayout_3.addWidget(self.weekly, 0, QtCore.Qt.AlignLeft)
        self.monthly = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.monthly.setMaximumSize(QtCore.QSize(60, 23))
        self.monthly.setCheckable(True)
        self.monthly.setAutoExclusive(True)
        self.monthly.setObjectName("monthly")
        self.horizontalLayout_3.addWidget(self.monthly)
        self.yearly = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.yearly.setMaximumSize(QtCore.QSize(60, 23))
        self.yearly.setCheckable(True)
        self.yearly.setAutoExclusive(True)
        self.yearly.setObjectName("yearly")
        self.horizontalLayout_3.addWidget(self.yearly)
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 411, 192))
        self.tableWidget.setMinimumSize(QtCore.QSize(411, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(411, 192))
        self.tableWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Frame)
        self.horizontalLayoutWidget_4.setGeometry(
            QtCore.QRect(130, 250, 201, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.reload_crons_btn = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_4)
        self.reload_crons_btn.setObjectName("reload_crons_btn")
        self.horizontalLayout_4.addWidget(self.reload_crons_btn)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Crontab GUI"))
        self.label.setText(_translate("Frame", "Crontab-GUI"))
        self.save_button.setText(_translate("Frame", "Save"))
        self.cancel_button.setText(_translate("Frame", "Close"))
        self.minute_input.setText(_translate("Frame", "*"))
        self.hour_input.setText(_translate("Frame", "*"))
        self.day_input.setText(_translate("Frame", "*"))
        self.month_input.setText(_translate("Frame", "*"))
        self.week_input.setText(_translate("Frame", "*"))
        self.label_6.setText(_translate("Frame", " Minute"))
        self.label_5.setText(_translate("Frame", " Hour"))
        self.label_4.setText(_translate("Frame", " Day"))
        self.label_3.setText(_translate("Frame", " Month"))
        self.label_2.setText(_translate("Frame", " Week"))
        self.add_button.setText(_translate("Frame", "Set"))
        self.label_7.setText(_translate("Frame", "Command: "))
        self.label_8.setText(_translate("Frame", "Job Preview:"))
        self.pushButton_7.setText(_translate("Frame", "Apply"))
        self.startup.setText(_translate("Frame", "Startup"))
        self.hourly.setText(_translate("Frame", "Hourly"))
        self.daily.setText(_translate("Frame", "Daily"))
        self.weekly.setText(_translate("Frame", "Weekly"))
        self.monthly.setText(_translate("Frame", "Monthly"))
        self.yearly.setText(_translate("Frame", "Yearly"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Command"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "Delete"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_8.setText(_translate("Frame", "BackUp"))
        self.reload_crons_btn.setText(_translate("Frame", "ReloadCrons"))

        """
        Custom section
        """

        self.cron_list = []
        self.iconDelete = QtWidgets.QWidget().style().standardIcon(
            getattr(QtWidgets.QStyle, "SP_TrashIcon"))
        self.iconEdit = QtWidgets.QWidget().style().standardIcon(
            getattr(QtWidgets.QStyle, "SP_DialogOkButton"))
        self.reload_crons_btn.clicked.connect(self.load_crons)
        self.crontab_file_name = "/tmp/crontab_file_list"
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 48)
        self.tableWidget.setColumnWidth(3, 48)
        self.new_cron_time = ""
        self.new_cront_job = ""
        self.command_input.textChanged.connect(lambda: self.changed_cron(''))
        self.startup.clicked.connect(lambda: self.changed_cron('@reboot'))
        self.yearly.clicked.connect(lambda: self.changed_cron('@yearly'))
        self.monthly.clicked.connect(lambda: self.changed_cron('@monthly'))
        self.weekly.clicked.connect(lambda: self.changed_cron('@weekly'))
        self.daily.clicked.connect(lambda: self.changed_cron('@daily'))
        self.hourly.clicked.connect(lambda: self.changed_cron('@hourly'))

        self.add_button.clicked.connect(self.set_custom_time)
        self.cancel_button.clicked.connect(sys.exit)
        self.pushButton_7.clicked.connect(self.handle_add_cron_button)
        self.save_button.clicked.connect(self.save_crons_to_file)
        self.pushButton_8.clicked.connect(self.back_up_crons)
        self.clean_files()

    def clean_files(self) -> None:
        try:
            os.remove(f"{self.crontab_file_name}")
            os.remove("/tmp/clean_crons")
        except:
            print("dont exist")

    def add_crons_new(self, crons: [[]]) -> None:
        for cron in crons:
            rows = self.tableWidget.rowCount()
            self.cron_list.append(cron)
            self.tableWidget.setRowCount(rows+1)
            self.tableWidget.setItem(
                rows, 0, QtWidgets.QTableWidgetItem(cron[0]))
            self.tableWidget.setItem(
                rows, 1, QtWidgets.QTableWidgetItem(cron[1]))
            self.tableWidget.setCellWidget(
                rows, 2, QtWidgets.QPushButton(self.iconEdit, ''))
            self.delete = QtWidgets.QPushButton(self.iconDelete, '')
            self.delete.clicked.connect(lambda: self.remove_cron(rows))
            self.tableWidget.setCellWidget(
                rows, 3, self.delete)

    def handle_add_cron_button(self) -> None:

        cron = self.lineEdit.text()
        times = ""
        if(self.lineEdit.text().startswith("@")):
            times = self.lineEdit.text().split(" ")[0]
        else:
            times = " ".join([
                self.minute_input.text(),
                self.hour_input.text(),
                self.day_input.text(),
                self.month_input.text(),
                self.week_input.text()
            ])
        command = self.command_input.text()
        if cron == '' or command == '':
            return
        isvalid = self.test_cron(cron)
        if isvalid == True:
            self.add_crons_new([[times, command]])
        else:
            QtWidgets.QMessageBox.warning(None, 'Syntax Error', isvalid)

    def load_crons(self) -> None:
        if self.cron_list:
            result = QtWidgets.QMessageBox.warning(None, 'Unchanged crons will be deleted',
                                                   'this is going to load only the crons from the file',
                                                   QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            if result != QtWidgets.QMessageBox.StandardButton.Ok:
                return

        self.clean_files()
        os.system(f"crontab -l > {self.crontab_file_name}")
        crons = []
        with open(f"{self.crontab_file_name}", "r") as f:
            lines = f.readlines()
            if(len(lines) == 0):
                return

            for i in lines:
                if i.startswith("#"):
                    continue

                i = i.replace("\n", "")
                splited = i.split(" ")
                if splited[0].startswith("@"):
                    crons.append(
                        [splited[0], " ".join(splited[1:])])
                elif splited[0] != '':
                    crons.append(
                        [" ".join(splited[:5]), " ".join(splited[5:])])

        if not crons:
            QtWidgets.QMessageBox.information(None,
                                              'No crons', 'this user has no crons')
            return

        self.clear_crons_gui()
        self.add_crons_new(crons)

    def changed_cron(self, time: str = '') -> None:
        self.new_cront_job = self.command_input.text()
        if time != '' and time != self.new_cron_time:
            self.new_cron_time = time
        self.lineEdit.setText(f"{self.new_cron_time} {self.new_cront_job}")

    def set_custom_time(self) -> None:
        times = " ".join([
            self.minute_input.text(),
            self.hour_input.text(),
            self.day_input.text(),
            self.week_input.text(),
            self.month_input.text(),
        ])
        self.changed_cron(times)

    def test_cron(self, cron: str) -> True or str:
        os.system('crontab -l > /tmp/goodcron')
        os.system(f'echo "{cron}" > /tmp/testcron')
        valid_cron = subprocess.Popen(
            ['crontab', '/tmp/testcron'], stderr=subprocess.PIPE)
        stderr = valid_cron.communicate()
        exit_code = valid_cron.wait()
        os.system('crontab /tmp/goodcron')
        if exit_code:
            error = " ".join(stderr[1].decode(
                'utf-8').split("\n")[0].split(' ')[1:])
            return error
        return True

    def remove_cron(self, row: int) -> None:
        self.tableWidget.removeRow(row)
        self.cron_list.pop(row)

    def clear_crons_gui(self) -> None:
        self.cron_list = []
        self.tableWidget.setRowCount(0)

    def save_crons_to_file(self) -> None:
        with open(self.crontab_file_name, 'w') as f:
            if self.cron_list:
                for i in self.cron_list:
                    f.write(" ".join([*i])+'\n')
            else:
                f.write('')

        save = subprocess.Popen(['crontab', self.crontab_file_name],
                                stderr=subprocess.PIPE)
        stderr = save.communicate()
        exit_code = save.wait()
        if exit_code:
            QtWidgets.QMessageBox.warning(
                None, 'Error saving file', stderr[1].decode('utf-8'))
            return
        QtWidgets.QMessageBox.information(
            None, 'Saved correctly', 'crons saved')

    def back_up_crons(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        try:
            with open(fileName, 'w') as f:
                for i in self.cron_list:
                    f.write(" ".join([*i])+'\n')
            QtWidgets.QMessageBox.information(
                None, 'Backup Saved', 'Backup saved Correctly')
        except PermissionError:
            QtWidgets.QMessageBox.warning(
                None, 'No permisions', 'this user dont have permisions to save the file here')
        except:
            QtWidgets.QMessageBox.warning(
                None, 'Error', 'Error was found cant save the file')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = crontab_gui()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
